# urls.py
from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PompeViewSet

router = DefaultRouter()
router.register(r'pompes', PompeViewSet)

app_name = 'pompe'
urlpatterns = [
    path('pompe_list/', views.PompeListView.as_view(), name='pompe_list'),
    path('pompe_create/', views.PompeCreateView.as_view(), name='pompe_create'),
    path('api/', include(router.urls)),
    path('pompe/<int:pk>/update/', views.PompeUpdateView.as_view(), name='pompe_update'),
     path('pompe/<int:pk>/deactivate/', views.PompeDeactivateView.as_view(), name='pompe_deactivate'),
      path('pompe/<int:pk>/reactivate/', views.PompeReactivateView.as_view(), name='cuve_reactivate'),
]
