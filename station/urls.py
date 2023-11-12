from django.urls import path
from .views import StationDeactivateView
from .views import (
    StationListView, 
    StationCreateView, 
    StationUpdateView, 
    StationDeactivateView,
    station_detail
)
app_name = 'station'
urlpatterns = [
    
    path('', StationListView.as_view(), name='station_list'),
    path('create/', StationCreateView.as_view(), name='station_create'),
    path('<int:pk>/update/', StationUpdateView.as_view(), name='station_update'),
    path('<int:pk>/deactivate/', StationDeactivateView.as_view(), name='station_deactivate'),
     path('<int:pk>/', station_detail, name='station_detail'), 
]


