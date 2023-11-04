# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pompe_list/', views.PompeListView.as_view(), name='pompe_list'),
    path('pompe_create/', views.PompeCreateView.as_view(), name='pompe_create'),
    path('pompe/<int:pk>/detail/', views.PompeDetailView.as_view(), name='pompe_detail'),
    path('pompe/<int:pk>/update/', views.PompeUpdateView.as_view(), name='pompe_update'),
    path('pompe/<int:pk>/delete/', views.PompeDeleteView.as_view(), name='pompe_delete'),
]
