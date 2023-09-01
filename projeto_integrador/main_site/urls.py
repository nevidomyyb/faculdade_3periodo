from django.urls import include, path
from main_site import views

app_name='main_site'

urlpatterns = [
    path('', views.home, name='home')
]