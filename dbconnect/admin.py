from django.contrib import admin

# Register your models here.
from .models import StlDistrict, StlDisciplineIncidents, StlDemographic, StlActScore, StlStudentStaffRatio

# Register each model
admin.site.register(StlDistrict)
admin.site.register(StlDisciplineIncidents)
admin.site.register(StlDemographic)
admin.site.register(StlActScore)
admin.site.register(StlStudentStaffRatio)