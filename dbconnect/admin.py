from django.contrib import admin

# Register your models here.
from .models import StlDistrict, StlDisciplineIncidents, StlDemographic, StlActScore, StlStudentStaffRatio

class StlDistrictAdmin(admin.ModelAdmin):
    fieldsets = [
        ("District", {"fields": ["county_district_code", "district_name"]}),
    ]
    list_display = ["county_district_code", "district_name"]
    search_fields = ["district_name"]

# Register each model
admin.site.register(StlDistrict, StlDistrictAdmin)
admin.site.register(StlDisciplineIncidents)
admin.site.register(StlDemographic)
admin.site.register(StlActScore)
admin.site.register(StlStudentStaffRatio)