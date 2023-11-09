
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('station/', include(('station.urls', 'station'), namespace='station')),
    path('cuve/', include(('cuve.urls', 'cuve'), namespace='cuve')),
    path('pompe/', include(('pompe.urls', 'pompe'), namespace='pompe')),
    path('pompiste/', include(('pompiste.urls', 'pompiste'), namespace='pompiste')),
    path('vents/', include('vents.urls')),
     path('users/', include('users.urls')), 
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)