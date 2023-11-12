# urls.py
from django.urls import path
from . import views
app_name = 'pompe'
urlpatterns = [
    path('pompe_list/', views.PompeListView.as_view(), name='pompe_list'),
    path('pompe_create/', views.PompeCreateView.as_view(), name='pompe_create'),
  
    path('pompe/<int:pk>/update/', views.PompeUpdateView.as_view(), name='pompe_update'),
     path('pompe/<int:pk>/deactivate/', views.PompeDeactivateView.as_view(), name='pompe_deactivate'),
      path('pompe/<int:pk>/reactivate/', views.PompeReactivateView.as_view(), name='cuve_reactivate'),
]
