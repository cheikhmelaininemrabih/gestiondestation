from django.urls import path
from .views import (PompisteListView, PompisteCreateView, PompisteUpdateView, PompisteDeleteView)

app_name = 'pompiste'

urlpatterns = [
    path('', PompisteListView.as_view(), name='pompiste_list'),
    path('create/', PompisteCreateView.as_view(), name='pompiste_create'),
    path('<int:pk>/update/', PompisteUpdateView.as_view(), name='pompiste_update'),
    path('<int:pk>/delete/', PompisteDeleteView.as_view(), name='pompiste_delete'),
]
