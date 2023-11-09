from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    
    path('station/', views.admin_dashboard, name='admin_dashboard'),
    path('responsable/', views.responsable_dashboard, name='responsable_dashboard'),
    # path('pompe_list/', views.pompiste_dashboard, name='pompiste_dashboard'),
    path('admin/activate_user/<int:user_id>/', views.admin_activate_user, name='admin_activate_user'),

]  
