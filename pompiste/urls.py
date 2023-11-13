from django.urls import path
from .views import PompisteDeactivateView
from .views import (PompisteListView, PompisteCreateView, PompisteUpdateView)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PompisteViewSet

router = DefaultRouter()
router.register(r'pompistes', PompisteViewSet)


app_name = 'pompiste'

urlpatterns = [
    path('api/', include(router.urls)),

    path('', PompisteListView.as_view(), name='pompiste_list'),
    path('create/', PompisteCreateView.as_view(), name='pompiste_create'),
    path('<int:pk>/update/', PompisteUpdateView.as_view(), name='pompiste_update'),
     path('<int:pk>/deactivate/', PompisteDeactivateView.as_view(), name='pompiste_deactivate'),
]
