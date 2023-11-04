from django.urls import path
from . import views

app_name = 'vents'

urlpatterns = [
    
    path('new/', views.create_vente, name='create_vente'),
    
]
