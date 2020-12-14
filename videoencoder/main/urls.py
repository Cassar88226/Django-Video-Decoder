from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

from . import views
from .views import GetDroplets
app_name = 'main'
urlpatterns = [
    path('log_in/', views.log_in, name='index'),
    path('', GetDroplets.as_view(template_name='droplets.html'), name='Droplet View'),

    path('sign_up/', views.signup, name ='signup'),
    path('log_out/', views.log_out, name='index'),
]
