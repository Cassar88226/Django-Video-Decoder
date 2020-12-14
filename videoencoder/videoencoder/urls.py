from django.contrib import admin
from django.urls import include, path
from main.views import GetDroplets
from django.conf.urls import url
from main import views


urlpatterns = [
    #path('', include('hello_world.urls')),
    path('admin/', admin.site.urls),
    path('', GetDroplets.as_view(template_name='droplets.html'), name='Droplet View'),
    url(r'^submit', views.submit)
]