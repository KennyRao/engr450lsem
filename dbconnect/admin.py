from django.contrib import admin

# Register your models here.
from .models import StlDistrict, StlDisciplineIncidents, StlDemographic, StlActScore, StlStudentStaffRatio

class StlDistrictAdmin(admin.ModelAdmin):
    list_display = ('county_district_code', 'district_name')
    search_fields = ('county_district_code', 'district_name')

class StlDisciplineIncidentsAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'discipline_incidents', 
        'discipline_incident_rate', 'discipline_alcohol_rate', 'discipline_drug_rate', 
        'discipline_other_rate', 'discipline_tobacco_rate', 'discipline_violence_rate', 
        'discipline_weapon_rate', 'discipline_removal_in_schl_susp_rate', 
        'discipline_removal_out_schl_susp_rate', 'discipline_removal_expulsion_rate', 
        'discipline_more_10_days_rate',
    )
    search_fields = ('year', 'county_district_code')

class StlDemographicAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'lunch_count_free_reduced_pct', 
        'enrollment_asian_pct', 'enrollment_asian_pacific_islander_pct', 'enrollment_black_pct', 
        'enrollment_hispanic_pct', 'enrollment_indian_pct', 'enrollment_multiracial_pct', 
        'enrollment_pacific_islander_pct', 'enrollment_white_pct', 
        'ell_lep_students_enrolled_k_12_pct', 'ell_lep_students_enrolled_pk_pct', 
        'iep_incidence_rate',
    )
    search_fields = ('year', 'county_district_code')

class StlActScoreAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'act_tests_administered', 'graduates', 
        'graduates_with_act_score_above_national_avg', 'graduates_with_act_score_above_national_avg_pct', 
        'graduates_who_took_act_and_scored_above_national_avg_pct', 'act_composite_score', 
        'act_english_score', 'act_math_score', 'act_reading_score', 'act_science_score',
    )
    search_fields = ('year', 'county_district_code')

class StlStudentStaffRatioAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'students_per_admin_ratio', 
        'students_per_classrm_tch_ratio', 'students_per_teacher_ratio',
    )
    search_fields = ('year', 'county_district_code')

# Register each model
admin.site.register(StlDistrict, StlDistrictAdmin)
admin.site.register(StlDisciplineIncidents, StlDisciplineIncidentsAdmin)
admin.site.register(StlDemographic, StlDemographicAdmin)
admin.site.register(StlActScore, StlActScoreAdmin)
admin.site.register(StlStudentStaffRatio, StlStudentStaffRatioAdmin)