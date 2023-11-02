from django.urls import path
from . import views

app_name = 'pompiste'

urlpatterns = [
    path('', views.PompisteListView.as_view(), name='pompiste_list'),
    path('create/', views.PompisteCreateView.as_view(), name='pompiste_create'),
    path('<int:pk>/', views.PompisteUpdateView.as_view(), name='pompiste_update'),
    path('<int:pk>/delete/', views.PompisteDeleteView.as_view(), name='pompiste_delete'),
]
