from django.urls import include, path
from main_site import views

app_name='main_site'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logoutAA, name='logout')
]