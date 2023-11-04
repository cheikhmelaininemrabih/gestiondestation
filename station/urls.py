from django.urls import path
from . import views

urlpatterns = [
    path('', views.StationListView.as_view(), name='station_list'),
    path('create/', views.StationCreateView.as_view(), name='station_create'),
    path('<int:pk>/update/', views.StationUpdateView.as_view(), name='station_update'),
    path('<int:pk>/delete/', views.StationDeleteView.as_view(), name='station_delete'),
]
