from django.urls import path
from .views import StationDeactivateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StationViewSet
from .views import (
    StationListView, 
    StationCreateView, 
    StationUpdateView, 
    StationDeactivateView,
    station_detail
)
router = DefaultRouter()

router.register(r'stations', StationViewSet)

app_name = 'station'
urlpatterns = [
    path('api/', include(router.urls)),
    
    path('', StationListView.as_view(), name='station_list'),
    path('create/', StationCreateView.as_view(), name='station_create'),
    path('<int:pk>/update/', StationUpdateView.as_view(), name='station_update'),
    path('<int:pk>/deactivate/', StationDeactivateView.as_view(), name='station_deactivate'),
     path('<int:pk>/', station_detail, name='station_detail'), 
]


