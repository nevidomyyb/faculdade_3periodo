from django.urls import include, path
from main_site.views.login_views import auth, login, logoutAA, register, perform_register
from main_site.views.general_views import home
from main_site.views.projeto_views import visualizar_projeto, editar_projeto,performar_editar_projeto, criar_projeto, performar_criar_projeto

app_name='main_site'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('auth/', auth, name='auth'),
    path('logout/', logoutAA, name='logout'),
    path('register/', register, name='register'),
    path('perform_register/', perform_register, name='perform_register'),
    path('projeto/<int:pk>/', visualizar_projeto, name='visualizar_projeto'),
    path('projeto/editar/<int:pk>/', editar_projeto, name='editar_projeto'),
    path('projeto/editar/performar/<int:pk>/', performar_editar_projeto, name='performar_editar_projeto'),
    path('projeto/criar/', criar_projeto, name='criar_projeto'),
    path('projeto/criar/performar/', performar_criar_projeto, name='criar_projeto_performar')
]