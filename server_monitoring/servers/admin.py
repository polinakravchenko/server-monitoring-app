from django.contrib import admin
from .models import Servers

class ServersAdmin(admin.ModelAdmin):
  list_display = ("server_name", "time_notification", "server_localization",)
  
admin.site.register(Servers, ServersAdmin)
# Register your models here.
