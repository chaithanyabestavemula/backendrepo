from django_filters import *
from .models import *


class studentfilters(FilterSet):
    acesscard=NumberFilter(field_name='acesscard',lookup_expr='gte')
    first_name=AllValuesFilter(field_name='first_name',lookup_expr='exact')



    class Meta:
        model = student
        fields = '__all__'
