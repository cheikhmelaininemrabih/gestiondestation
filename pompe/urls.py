from django.urls import path
from . import views

urlpatterns = [
    path('', views.PompeListView.as_view(), name='pompe_list'),
    path('create/', views.PompeCreateView.as_view(), name='pompe_create'),
    path('<int:pk>/', views.PompeDetailView.as_view(), name='pompe_detail'),
    path('<int:pk>/update/', views.PompeUpdateView.as_view(), name='pompe_update'),
    path('<int:pk>/delete/', views.PompeDeleteView.as_view(), name='pompe_delete'),
]
