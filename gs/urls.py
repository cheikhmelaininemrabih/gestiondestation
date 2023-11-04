
from django.contrib import admin
from django.urls import path , include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('station/', include('station.urls')),
    path('cuve/', include('cuve.urls')),
    path('pompe/', include('pompe.urls')),
    path('pompiste/', include('pompiste.urls')),

]