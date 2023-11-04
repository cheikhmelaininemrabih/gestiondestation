from django.urls import path
from .views import (
    StationListView, 
    StationCreateView, 
    StationUpdateView, 
    StationDeleteView
)
app_name = 'station'
urlpatterns = [
    
    path('', StationListView.as_view(), name='station_list'),
    path('create/', StationCreateView.as_view(), name='station_create'),
    path('<int:pk>/update/', StationUpdateView.as_view(), name='station_update'),
    path('<int:pk>/delete/', StationDeleteView.as_view(), name='station_delete'),
]
