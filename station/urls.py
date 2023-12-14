from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StationViewSet, StationListView, StationCreateView, 
    StationUpdateView, StationDeactivateView, station_detail
)

router = DefaultRouter()
router.register(r'stations', StationViewSet)

app_name = 'station'
api_urlpatterns = [
    path('api/', include(router.urls)),
]
web_urlpatterns = [
    
    path('', StationListView.as_view(), name='station_list'),
    path('create/', StationCreateView.as_view(), name='station_create'),
    path('<int:pk>/update/', StationUpdateView.as_view(), name='station_update'),
    path('<int:pk>/deactivate/', StationDeactivateView.as_view(), name='station_deactivate'),
    path('<int:pk>/', station_detail, name='station_detail'), 
]
urlpatterns = web_urlpatterns + api_urlpatterns