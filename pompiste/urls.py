# pompiste/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PompisteViewSet, PompisteListView, PompisteCreateView, PompisteUpdateView, PompisteDeactivateView

router = DefaultRouter()
router.register(r'', PompisteViewSet)

app_name = 'pompiste'

# API URLs
api_urlpatterns = [
    path('', include(router.urls)),
]

# Regular web view URLs
web_urlpatterns = [
    path('list/', PompisteListView.as_view(), name='pompiste_list'),
    path('create/', PompisteCreateView.as_view(), name='pompiste_create'),
    path('create/<int:station_id>/', PompisteCreateView.as_view(), name='pompiste_create_with_station'),
    path('<int:pk>/update/', PompisteUpdateView.as_view(), name='pompiste_update'),
    path('<int:pk>/deactivate/', PompisteDeactivateView.as_view(), name='pompiste_deactivate'),
]

urlpatterns = api_urlpatterns + web_urlpatterns
