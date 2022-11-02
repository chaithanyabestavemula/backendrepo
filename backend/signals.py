from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save


def login(sender,request,user,**kwargs):
    print("-----login----")
    print("sentby:" ,sender)

    print("reque :", request)
    print("user :", user)
    print(f'kwargs:{kwargs}')

user_logged_in.connect(login,sender=User)

@receiver(user_logged_out,sender=User)
def logout(sender,request,user,**kwargs):
    print("------logout---")
    print("sentby:" ,sender)

    print("reque :", request)
    print("user :", user)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def loginfailed(sender,credentials,request,**kwargs):
    print("-----loginfailed----")
    print("sentby:" ,sender)


    print("reque :", request)
    print("credentials:",credentials)
    print(f'kwargs:{kwargs}')
@receiver(pre_save,sender=User)
def usercreate(sender,instance,**kwargs):
    print("-----user created---")
    print("sentby:", sender)

    print("instanced :", instance)

    print(f'kwargs:{kwargs}')




