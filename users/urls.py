from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, sing_in, sing_up, activate_user, role_user, pompiste_dashbord, responsable_dashbord
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)



urlpatterns = [
    path('api/', include(router.urls)),

    path('', dashboard, name='dashboard'),
    path('login/', sing_in, name='sing_in'),
    path('register/', sing_up, name='sing_up'),
    path('responsable_dashbord/', responsable_dashbord, name='responsable_dashbord'),
    path('pompiste_dashbord/', pompiste_dashbord, name='pompiste_dashbord'),
    path('activate_user/<int:user_id>/', activate_user, name='activate_user'),
    path('role_user/<int:user_id>/', role_user, name='role_user'),
]  

