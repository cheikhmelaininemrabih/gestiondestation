

from django.urls import path
from . import views
from .views import (
    CuveListView,
    CuveCreateView,
    CuveUpdateView,
    
)

app_name = 'cuve'

urlpatterns = [
    path('', CuveListView.as_view(), name='cuve_list'),
    path('create/', CuveCreateView.as_view(), name='cuve_create'),
    path('<int:pk>/update/', CuveUpdateView.as_view(), name='cuve_update'),
    path('cuve/<int:pk>/deactivate/', views.CuveDeactivateView.as_view(), name='cuve_deactivate'),
    path('cuve/<int:pk>/reactivate/', views.CuveReactivateView.as_view(), name='cuve_reactivate'),
]
