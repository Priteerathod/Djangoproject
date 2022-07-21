from django.contrib import admin
from testapp.models import client
# Register your models here.
class clientAdmin(admin.ModelAdmin):
    list_display=['cid','cname','cdate','cby']
admin.site.register(client,clientAdmin)
