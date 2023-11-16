

from django.urls import path
from . import views
from django.urls import path, include
from .views import (
    CuveListView,
    CuveCreateView,
    CuveUpdateView,
    
)
from rest_framework.routers import DefaultRouter
from .views import CuveViewSet

router = DefaultRouter()
router.register(r'cuves', CuveViewSet)
app_name = 'cuve.apps.CuveConfig'

urlpatterns = [
    path('', CuveListView.as_view(), name='cuve_list'),
    # path('create/', CuveCreateView.as_view(), name='cuve_create'),
    path('create/<int:station_id>/', CuveCreateView.as_view(), name='cuve_create'),

    path('', include(router.urls)),
    path('create/', CuveCreateView.as_view(), name='cuve_create'),
    path('<int:pk>/update/', CuveUpdateView.as_view(), name='cuve_update'),
    path('cuve/<int:pk>/deactivate/', views.CuveDeactivateView.as_view(), name='cuve_deactivate'),
    path('cuve/<int:pk>/reactivate/', views.CuveReactivateView.as_view(), name='cuve_reactivate'),
]
