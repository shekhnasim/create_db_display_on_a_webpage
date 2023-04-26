from django.contrib import admin
from . models import Site
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
@admin.register(Site)
#class SiteModelAdmin(admin.ModelAdmin):
    #list_display=['SiteName','Cluster','Sector','CellName','Band','AntennaHeight','Azimuth']

class sitedata(ImportExportActionModelAdmin):
    pass