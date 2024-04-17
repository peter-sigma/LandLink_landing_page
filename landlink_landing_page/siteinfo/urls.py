from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
app_name='siteinfo'

urlpatterns = [
    path('', views.home, name='home'),
    
]