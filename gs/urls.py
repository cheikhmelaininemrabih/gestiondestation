# Inside your_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('station/', include(('station.urls', 'station'), namespace='station')),
    path('cuve/', include(('cuve.urls', 'cuve'), namespace='cuve')),
    path('pompe/', include(('pompe.urls', 'pompe'), namespace='pompe')),
    path('pompiste/', include(('pompiste.urls', 'pompiste'), namespace='pompiste')),
]
