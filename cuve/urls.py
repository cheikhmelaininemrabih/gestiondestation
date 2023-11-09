

from django.urls import path
from .views import (
    CuveListView,
    CuveCreateView,
    CuveUpdateView,
    CuveDeleteView,
)

app_name = 'cuve'

urlpatterns = [
    path('', CuveListView.as_view(), name='cuve_list'),
    path('create/', CuveCreateView.as_view(), name='cuve_create'),
    path('<int:pk>/update/', CuveUpdateView.as_view(), name='cuve_update'),
    path('<int:pk>/delete/', CuveDeleteView.as_view(), name='cuve_delete'),
]
