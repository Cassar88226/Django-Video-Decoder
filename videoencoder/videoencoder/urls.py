from django.contrib import admin
from django.urls import include, path
from main.views import GetDroplets
from django.conf.urls import url
from main import views


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    url(r'^submit', views.submit)
]