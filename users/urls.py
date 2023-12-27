from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, delete_user, sing_in, sing_up, activate_user, role_user, pompiste_dashbord, responsable_dashbord
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
api_urlpatterns = [
     path('api/', include(router.urls)),
]
web_urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sing_in')), name='logout'),
     path('admin_signup/', lambda request: sing_up(request, admin_creation=True), name='admin_sing_up'),
     path('modify_user/<int:user_id>/', views.modify_user, name='modify_user'),
    path('login/', sing_in, name='sing_in'),
    path('register/', sing_up, name='sing_up'),
    path('station/<int:station_id>/add_pompe/', views.add_pompe_to_station, name='add_pompe_to_station'),
    path('station/<int:station_id>/add_cuve/', views.add_cuve_to_station, name='add_cuve_to_station'),

    path('assign_pompiste/<int:station_id>/', views.assign_pompiste_to_station, name='assign_pompiste_to_station'),
     path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('responsable_dashbord/', responsable_dashbord, name='responsable_dashbord'),
    path('pompiste_dashbord/', pompiste_dashbord, name='pompiste_dashbord'),
    path('activate_user/<int:user_id>/', activate_user, name='activate_user'),
    path('role_user/<int:user_id>/', role_user, name='role_user'),
]  
urlpatterns = api_urlpatterns + web_urlpatterns