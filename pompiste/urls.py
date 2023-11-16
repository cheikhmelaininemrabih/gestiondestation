from django.urls import path
from .views import PompisteDeactivateView
from .views import (PompisteListView, PompisteCreateView, PompisteUpdateView)

app_name = 'pompiste'

urlpatterns = [
    path('', PompisteListView.as_view(), name='pompiste_list'),
    # path('create/', PompisteCreateView.as_view(), name='pompiste_create'),
    path('create/<int:station_id>/', PompisteCreateView.as_view(), name='pompiste_create'),

    path('<int:pk>/update/', PompisteUpdateView.as_view(), name='pompiste_update'),
    path('<int:pk>/deactivate/', PompisteDeactivateView.as_view(), name='pompiste_deactivate'),
]
