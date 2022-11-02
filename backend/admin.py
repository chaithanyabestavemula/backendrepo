from django.contrib import admin
from .models import *
admin.site.register(vehicle)
admin.site.register(car)
admin.site.register(truck)
admin.site.register(club)
admin.site.register(department)
admin.site.register(library)
admin.site.register(student)
admin.site.register(fileupload)
admin.site.register(fruits)
from django.contrib.sessions.models import Session


admin.site.register(Session)
@admin.register(customer)
class customeradmin(admin.ModelAdmin):
    list_display = ('name','amount')




# Register your models here.
