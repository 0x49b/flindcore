from django.contrib import admin
from .models import Proxy


# Register your models here.
@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    ordering = ('-last_checked', )
    list_display = ('ip_address', 'port', 'code', 'country', 'anonimity', 'google', 'https', 'last_checked')
