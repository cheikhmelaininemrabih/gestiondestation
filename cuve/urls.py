from django.urls import path
from . import views

app_name = 'cuve'

urlpatterns = [
    path('cuve/', views.CuveListView.as_view(), name='cuve_list'),
    path('create/', views.CuveCreateView.as_view(), name='cuve_create'),
   
    path('<int:pk>/update/', views.CuveUpdateView.as_view(), name='cuve_update'),
    path('<int:pk>/delete/', views.CuveDeleteView.as_view(), name='cuve_delete'),
]
