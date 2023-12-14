from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pompes', views.PompeViewSet)

app_name = 'pompe'
api_urlpatterns = [
 path('', include(router.urls)),  
]
web_urlpatterns = [
   # Include REST framework URLs
    path('list/', views.PompeListView.as_view(), name='pompe_list'),
    path('create/', views.PompeCreateView.as_view(), name='pompe_create'),
    path('create/<int:station_id>/', views.PompeCreateView.as_view(), name='pompe_create_with_station'),
    path('<int:pk>/update/', views.PompeUpdateView.as_view(), name='pompe_update'),
    path('<int:pk>/deactivate/', views.PompeDeactivateView.as_view(), name='pompe_deactivate'),
    path('<int:pk>/reactivate/', views.PompeReactivateView.as_view(), name='pompe_reactivate'),
]
urlpatterns = web_urlpatterns + api_urlpatterns