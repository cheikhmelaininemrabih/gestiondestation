<<<<<<< HEAD
# cuve/urls.py
from django.urls import path
from .views import CuveListView, CuveCreateView, CuveUpdateView, CuveDeleteView
=======
# from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
>>>>>>> beae8d7bf4da31ceaba9ddf8e2fb7f459485c1b4

app_name = 'cuve'
urlpatterns = [
<<<<<<< HEAD
    path('', CuveListView.as_view(), name='cuve_list'),
    path('create/', CuveCreateView.as_view(), name='cuve_create'),
    path('<int:pk>/update/', CuveUpdateView.as_view(), name='cuve_update'),
    path('<int:pk>/delete/', CuveDeleteView.as_view(), name='cuve_delete'),
=======
    path('cuve_list/', views.CuveListView.as_view(), name='cuve_list'),
    path('create/', views.CuveCreateView.as_view(), name='cuve_create'),
   
    path('<int:pk>/update/', views.CuveUpdateView.as_view(), name='cuve_update'),
    path('<int:pk>/delete/', views.CuveDeleteView.as_view(), name='cuve_delete'),
>>>>>>> beae8d7bf4da31ceaba9ddf8e2fb7f459485c1b4
]
