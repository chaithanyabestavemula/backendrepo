from django.contrib import admin
from django.urls import path,include, re_path
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as vi
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page
import debug_toolbar
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router=DefaultRouter()
router.register('apiveh',views.vehviewset)
router.register('apicar',views.carviewset)
router.register('apitruck',views.truckviewset)
router.register('apifiles',views.files)
router.register('apitrans',views.transaction)
router.register('apistudent',views.studentview)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiclereg/',views.home),
    path('hello',views.homer),
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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('studentdetails/',views.studentdetails),


]
# urlpatterns = format_suffix_patterns(urlpatterns)
