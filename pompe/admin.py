from django.contrib import admin
from .models import Pompe

@admin.register(Pompe)
class PompeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'model', 'id_cuve', 'id_pompiste')
