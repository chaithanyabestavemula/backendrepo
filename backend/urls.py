from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as vi
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page
import debug_toolbar


router=DefaultRouter()
router.register('apiveh',views.vehviewset)
router.register('apicar/',views.carviewset)
router.register('apitruck/',views.truckviewset)
router.register('apifiles',views.files)
router.register('apitrans',views.transaction)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiclereg/',views.home),
    path('',views.homer),
    path('carsreg/',views.carview),
    path('truckreg/',views.truckview),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('payment/',views.paymentview),
    path('upload/',views.uploadview),
    path('api-token-auth/',vi.obtain_auth_token),
    path('orm/<pk>/',views.ormview),
    path('ormclass/<pk>/',views.ormclass.as_view()),
    path('scenario11/<int:pk>/',views.scenario11.as_view()),
    path('vehapiview/',views.vehapiview),
    path('scenario2/',views.scenario2),
    path('scenario1/<int:pk>/',views.scenario1.as_view()),
    path('scenario5/',views.scenario5.as_view()),
    path('scenario6/',views.scenario6.as_view()),
    path('scenario9/',views.scenario9.as_view()),
    path('sleep/',views.sleep),
    path('cache/',views.first),
    path('cachejson/',cache_page(60*2)(views.allreturn.as_view())),
    path('__debug__/', include(debug_toolbar.urls)),


]
