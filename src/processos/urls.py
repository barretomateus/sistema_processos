from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.Registro.as_view(), name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('processos/', views.get_user_processos, name='processos'),
    path('processos/new/', views.add_user_processo, name='add_processos'),
    path('processos/<int:id_processo>/view/', views.view_user_processo, name='view_processo'),
    path('processos/<int:id_processo>/view/requerimento/', views.requerimento, name='requerimento'),
    path('processos/<int:id_processo>/edit/', views.edit_user_processo, name='edit_processo'),
    path('processos/clone/', views.clone_user_processo, name='clone_processo'),
    path('processos/remove/', views.remove_user_processo, name='remove_process'),
    path('dados/', views.get_user_data, name='user_data'),
    path('dados/new/', views.add_user_data, name='add_user_data'),
    path('dados/<int:id_data>/edit/', views.edit_user_data, name='edit_user_data'),
    # path('dados/<int:id>/', views.add_edit_user_data, name='add_edit_user_data')
]
