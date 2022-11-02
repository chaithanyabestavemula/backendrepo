from rest_framework import serializers
from .models import *

class vehser(serializers.ModelSerializer):
    class Meta:
        model=vehicle
        fields='__all__'
        lookup_field=('pk','model')

class carser(serializers.ModelSerializer):
    class Meta:
        model=car
        fields='__all__'

class truckser(serializers.ModelSerializer):
    class Meta:
        model=truck
        fields='__all__'
        lookup_field='model'
class uploadser(serializers.ModelSerializer):
    class Meta:
        model=fileupload
        fields='__all__'
class transer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields='__all__'

class studentser(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
class deptser(serializers.ModelSerializer):
    class Meta:
        model=department
        fields='__all__'






