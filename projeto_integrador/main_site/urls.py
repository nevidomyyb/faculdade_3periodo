from django.urls import include, path
from main_site.views.login_views import auth, login, logoutAA, register, perform_register
from main_site.views.general_views import home

app_name='main_site'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('auth/', auth, name='auth'),
    path('logout/', logoutAA, name='logout'),
    path('register/', register, name='register'),
    path('perform_register/', perform_register, name='perform_register'),
]