
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include






urlpatterns = [
    path('api/', include('cuve.urls')),

    path('admin/', admin.site.urls),
    path('station/', include(('station.urls', 'station'), namespace='station')),
    path('cuve/', include(('cuve.urls', 'cuve'), namespace='cuve')),
    path('pompe/', include(('pompe.urls', 'pompe'), namespace='pompe')),
    path('pompiste/', include(('pompiste.urls', 'pompiste'), namespace='pompiste')),
    path('vents/', include('vents.urls')),
    path('users/', include('users.urls')), 
    # path('cuve/create/<int:station_id>/', views.CuveCreateView.as_view(), name='cuve_create'),
    # path('pompe/create/<int:station_id>/', views.PompeCreateView.as_view(), name='pompe_create'),
    # path('pompiste/create/<int:station_id>/', views.PompisteCreateView.as_view(), name='pompiste_create'),
   
     
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)