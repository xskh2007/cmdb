from django.contrib import admin
from hostinfo.models import Host

class HostAdmin(admin.ModelAdmin):
    list_display = [
                'hostname',
                'ip',
                'osversion',
                'memory',
                'disk',
                # 'vendor_id',
                # 'model_name',
                # 'cpu_core',
                # 'product',
                # 'Manufacturer',
                # 'sn'
          ]

admin.site.register(Host,HostAdmin)
