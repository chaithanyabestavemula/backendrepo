from django.shortcuts import render
from rest_framework.response import Response

from django.http import HttpResponse,JsonResponse
from .forms import *
from rest_framework.decorators import api_view
from django.db.models import F
from django.db import connection
from rest_framework.authtoken.views import APIView
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .filters import *
import time
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.db import transaction
from rest_framework.generics import *
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,CreateModelMixin
from rest_framework import status





def homer(request):
    return render(request, 'home.html')

@csrf_protect
def home(request):
    context = {}

    form = veh(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        print(form.cleaned_data['model'])
    context['form'] = veh()
    return render(request,'base.html',context)

@csrf_protect
def carview(request):
    context = {}

    form = carform(request.POST  or None,request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    context['form'] = carform()
    return render(request,'base.html',context)


def truckview(request):
    context = {}

    form = truckform(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
    context['form'] = truckform()
    return render(request,'base.html',context)


class vehviewset(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = vehser
    lookup_field = ('model')
    filterset_fields = ['wheelcount','model']

    search_fields = ['model']
    #p=Paginator(queryset,4)



    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class carviewset(viewsets.ModelViewSet):
    queryset = car.objects.all()
    serializer_class = carser
    filterset_fields = ['wheelcount', 'model']

    search_fields = ['model']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class truckviewset(viewsets.ModelViewSet):
    queryset = truck.objects.all()
    serializer_class = truckser
    filterset_fields = ['wheelcount', 'model']

    search_fields = ['model']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
def paymentview(request):
    context = {}

    form = paymentform(request.POST)
    if request.method == 'POST' and form.is_valid():
        x = form.cleaned_data['name']
        y = form.cleaned_data['paidto']
        z = int(form.cleaned_data['amount'])

        try:


            with transaction.atomic():

                    payor = customer.objects.get(name=x)
                    payor.amount-= z
                    payor.save()
                    paidto = customer.objects.get(name=y)
                    paidto.amount+=z
                    paidto.save()
        except:
            return HttpResponse("invalid credentials")


    context['form'] = paymentform()
    return render(request,'base.html',context)
def uploadview(request):
    context = {}

    #form = uploadform(request.POST,request.FILES)
    if request.method == 'POST':
        fileupload()

        form = uploadform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        else:
            uploadform()




    context['form'] = uploadform()
    return render(request, 'base.html', context)
def ormview(request,pk ):
    queryset = vehicle.objects.values().get(id=pk)
    serializer = vehser(queryset)
    print(request.GET)

    return JsonResponse(serializer.data)

class ormclass(GenericAPIView,RetrieveModelMixin):
    queryset = vehicle.objects.all()

    serializer_class = vehser

    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class scenario11(RetrieveAPIView):
    serializer_class = vehser
    def get_queryset(self):
        if self.request.method == 'GET':
            print((self.request.GET['model']))
            print((self.request.GET))

            queryset = vehicle.objects.all()

            model_name = self.request.GET.get('model',None)
            if model_name is not None:
                queryset = queryset.filter(model__exact=model_name)

            return queryset
class files(viewsets.ModelViewSet):
    queryset = fileupload.objects.all()
    serializer_class = uploadser
class transaction(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = transer


@api_view(['GET','POST'])
def vehapiview(request):
    query = vehicle.objects.all()
    serializer = vehser(data=request.data)
    print(request.data)
    print(request.data.get('model'))
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def scenario2(request):                #------scenario2
    queryset = student.objects.annotate(eroll=F('id')+100).order_by('eroll').values('eroll')
    serial = studentser(queryset)

    return Response(queryset)

class scenario1(RetrieveAPIView):
    serializer_class = studentser

    def get_queryset(self):
        if self.request.method == 'GET':
            #id=self.request.query_params.get('id',None)
            nam = self.request.query_params.get('name',None)
            queryset = student.objects.filter(last_name__endswith=nam)
            p = student.objects.values().filter(last_name__endswith=nam)
            q = p[0].get('dept_id')
            print(department.objects.values().get(pk=q))
            serializer_class = studentser(queryset)
            print(len(connection.queries))
            return queryset
class scenario5(ListCreateAPIView):
    serializer_class = studentser
    def post(self,request,*args,**kwargs):
        if self.request.method == 'POST':
            p = request.POST.get('l')
            p = p[1:-1]
            p = list(p.split(","))
            for i in p:
                print(i)
            q = student.objects.filter(first_name__in=p).count()
            return HttpResponse("print")
class scenario6(ListCreateAPIView):   #------scenario7----------scenario8
    serializer_class = studentser

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = student.objects.all()

            for i in queryset:
                print(i.id)
                print(i.dept)
                print(i.acesscard)
            print(len(connection.queries))

            '''queryset1=student.objects.all().values()
            print(queryset1)
            queryset2= student.objects.all().values_list()
            print(queryset2)
            queryset3 = student.objects.select_related()
            print(queryset3)
            queryset4 = student.objects.prefetch_related()
            print(queryset4)
            print(len(connection.queries))
            qs5=student.objects.only("first_name")
            print(qs5)
            print(len(connection.queries))'''


            return queryset
class scenario9(APIView):        #-------------------scenario9
    permission_classes = [AllowAny]

    def post(self,request):
        id = self.request.data.get('id',None)
        name = self.request.data.get('name',None)

        if id is not None:
            v = department.objects.get(pk=id)
            v.branch = name
            v.save()
            return Response(data="updated")
        else:
            v = department(id=id,branch=name)
            v.save()
            return Response(data="created")
def sleep(request):
    print("before sleep")
    time.sleep(10)
    print("after sleep")
    return HttpResponse("done")
def first(request):
    payload = []
    db = None
    if cache.get('fruits'):
        payload=cache.get('fruits')
        db = 'redis'
    else:
        queryset = fruits.objects.all()
        for i in queryset:
            payload.append(i.name)
        cache.set('fruits',payload)
        db = 'sqlite'
    return JsonResponse({'status' : 200 , 'db':db,'data':payload})

class allreturn(APIView):
    def get(self,*args):
        v = vehicle.objects.all()
        s = student.objects.all()
        c = customer.objects.all()
        vehserial = vehser(v,many=True)
        studentserial = studentser(s,many=True)
        customerser = transer(c,many=True)
        res={'vehserial':vehserial.data,'studentserial':studentserial.data,'customerser':customerser.data}
        return Response(res)
class studentview(viewsets.ModelViewSet):
    name = 'studentlist'


    queryset = student.objects.all()
    serializer_class = studentser
    filterset_class = studentfilters
    search_fields=['first_name']

@api_view(['GET','POST','DELETE'])
def studentdetails(request ):
    # try:
    #     s=student.objects.get(pk)
    # except student.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = student.objects.all()
        serializer = studentser(s,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = studentser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method=='DELETE':
    #     #s=student.objects.get(pk=pk)
    #     s.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)









































