from django import forms
from .models import *

class veh(forms.ModelForm):
    class Meta:
        model=vehicle
        fields='__all__'

class carform(forms.ModelForm):
    class Meta:
        model=car
        fields='__all__'

class truckform(forms.ModelForm):
    class Meta:
        model=truck
        fields='__all__'
class paymentform(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'
    paidto=forms.CharField(max_length=30)
class uploadform(forms.ModelForm):
    class Meta:
        model=fileupload
        fields='__all__'




