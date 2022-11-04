from django.db import models
class vehicle(models.Model):
    lp_number=models.IntegerField(null=True)
    wheelcount=models.IntegerField(null=True)
    manufacturer=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    class Meta:
        indexes=[models.Index(fields=['model'])]
    def __str__(self):
        return self.model

class car(vehicle):
    isairconditioned=models.BooleanField(default=False)
    hasrooftop=models.BooleanField(default=False)
    image=models.FileField(upload_to="",null=True)
    def __str__(self):
        return self.model
class truck(vehicle):
    maxgoodsweight=models.IntegerField(null=True)
    def __str__(self):
        return self.model

class department(models.Model):
    branch=models.CharField(max_length=30)

    def __str__(self):
        return self.branch
class club(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title
class library(models.Model):
    acesscard=models.IntegerField(null=False)

    def __str__(self):
        return str(self.acesscard)

class student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    dept=models.ForeignKey(department,on_delete=models.PROTECT)  #------manyto one
    club=models.ManyToManyField(club)  # ------manytomany with clubs
    acesscard=models.OneToOneField(library,null=True,on_delete=models.SET_NULL)# ---one to one

    def __str__(self):
        return self.first_name+" "+self.last_name
class customer(models.Model):
    name=models.CharField(max_length=40)
    amount=models.IntegerField(null=False)
class fileupload(models.Model):
    name=models.CharField(max_length=30)
    file=models.FileField(upload_to="")
    def __str__(self):
        return self.name

class fruits(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name












# Create your models here.
