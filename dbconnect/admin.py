from django.contrib import admin
from .models import StlDistrict, StlDisciplineIncidents, StlDemographic, StlActScore, StlStudentStaffRatio

class StlDistrictAdmin(admin.ModelAdmin):
    list_display = ('county_district_code', 'district_name')
    search_fields = ('county_district_code', 'district_name')

class StlDisciplineIncidentsAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'enrollment_grades_k_12', 'discipline_incidents', 
        'discipline_incident_rate_display', 'discipline_alcohol_rate_display', 'discipline_drug_rate_display', 
        'discipline_other_rate_display', 'discipline_tobacco_rate_display', 'discipline_violence_rate_display', 
        'discipline_weapon_rate_display', 'discipline_removal_in_schl_susp_rate_display', 
        'discipline_removal_out_schl_susp_rate_display', 'discipline_removal_expulsion_rate_display', 
        'discipline_more_10_days_rate_display',
    )
    search_fields = ('year', 'county_district_code')

    # Custom methods to display count and percentage
    def discipline_incident_rate_display(self, obj):
        return f"{obj.discipline_incidents} ({obj.discipline_incident_rate:.2f}%)"
    discipline_incident_rate_display.admin_order_field = 'discipline_incident_rate'  # Allows sorting by the rate

    def discipline_alcohol_rate_display(self, obj):
        return f"{obj.discipline_alcohol} ({obj.discipline_alcohol_rate:.2f}%)"

    def discipline_drug_rate_display(self, obj):
        return f"{obj.discipline_drug} ({obj.discipline_drug_rate:.2f}%)"

    def discipline_other_rate_display(self, obj):
        return f"{obj.discipline_other} ({obj.discipline_other_rate:.2f}%)"

    def discipline_tobacco_rate_display(self, obj):
        return f"{obj.discipline_tobacco} ({obj.discipline_tobacco_rate:.2f}%)"

    def discipline_violence_rate_display(self, obj):
        return f"{obj.discipline_violence} ({obj.discipline_violence_rate:.2f}%)"

    def discipline_weapon_rate_display(self, obj):
        return f"{obj.discipline_weapon} ({obj.discipline_weapon_rate:.2f}%)"

    def discipline_removal_in_schl_susp_rate_display(self, obj):
        return f"{obj.discipline_removal_in_schl_susp} ({obj.discipline_removal_in_schl_susp_rate:.2f}%)"

    def discipline_removal_out_schl_susp_rate_display(self, obj):
        return f"{obj.discipline_removal_out_schl_susp} ({obj.discipline_removal_out_schl_susp_rate:.2f}%)"

    def discipline_removal_expulsion_rate_display(self, obj):
        return f"{obj.discipline_removal_expulsion} ({obj.discipline_removal_expulsion_rate:.2f}%)"

    def discipline_more_10_days_rate_display(self, obj):
        return f"{obj.discipline_more_10_days} ({obj.discipline_more_10_days_rate:.2f}%)"

class StlDemographicAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'enrollment_grades_k_12', 'january_membership', 'lunch_count_free_reduced_display', 
        'enrollment_asian_display', 'enrollment_asian_pacific_islander_display', 'enrollment_black_display', 
        'enrollment_hispanic_display', 'enrollment_indian_display', 'enrollment_multiracial_display', 
        'enrollment_pacific_islander_display', 'enrollment_white_display', 
        'ell_lep_students_enrolled_k_12_display', 'ell_lep_students_enrolled_pk_display', 
        'iep_incidence_rate_display',
    )
    search_fields = ('year', 'county_district_code')

    # Custom methods to display count and percentage
    def lunch_count_free_reduced_display(self, obj):
        return f"{obj.lunch_count_free_reduced} ({obj.lunch_count_free_reduced_pct:.2f}%)"

    def enrollment_asian_display(self, obj):
        return f"{obj.enrollment_asian} ({obj.enrollment_asian_pct:.2f}%)"

    def enrollment_asian_pacific_islander_display(self, obj):
        return f"{obj.enrollment_asian_pacific_islander} ({obj.enrollment_asian_pacific_islander_pct:.2f}%)"

    def enrollment_black_display(self, obj):
        return f"{obj.enrollment_black} ({obj.enrollment_black_pct:.2f}%)"

    def enrollment_hispanic_display(self, obj):
        return f"{obj.enrollment_hispanic} ({obj.enrollment_hispanic_pct:.2f}%)"

    def enrollment_indian_display(self, obj):
        return f"{obj.enrollment_indian} ({obj.enrollment_indian_pct:.2f}%)"

    def enrollment_multiracial_display(self, obj):
        return f"{obj.enrollment_multiracial} ({obj.enrollment_multiracial_pct:.2f}%)"

    def enrollment_pacific_islander_display(self, obj):
        return f"{obj.enrollment_pacific_islander} ({obj.enrollment_pacific_islander_pct:.2f}%)"

    def enrollment_white_display(self, obj):
        return f"{obj.enrollment_white} ({obj.enrollment_white_pct:.2f}%)"

    def ell_lep_students_enrolled_k_12_display(self, obj):
        return f"{obj.ell_lep_students_enrolled_k_12} ({obj.ell_lep_students_enrolled_k_12_pct:.2f}%)"

    def ell_lep_students_enrolled_pk_display(self, obj):
        return f"{obj.ell_lep_students_enrolled_pk} ({obj.ell_lep_students_enrolled_pk_pct:.2f}%)"

    def iep_incidence_rate_display(self, obj):
        return f"{obj.iep_schoolage_childcount} ({obj.iep_incidence_rate:.2f}%)"

class StlActScoreAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'county_district_code', 'act_tests_administered', 'graduates', 
        'graduates_with_act_score_above_national_avg_display', 
        'graduates_who_took_act_and_scored_above_national_avg_display', 
        'act_composite_score', 'act_english_score', 'act_math_score', 
        'act_reading_score', 'act_science_score',
    )
    search_fields = ('year', 'county_district_code')

    # Custom methods to display count and percentage
    def graduates_with_act_score_above_national_avg_display(self, obj):
        return f"{obj.graduates_with_act_score_above_national_avg} ({obj.graduates_with_act_score_above_national_avg_pct:.2f}%)"

    def graduates_who_took_act_and_scored_above_national_avg_display(self, obj):
        return f"{obj.graduates_with_act_score_above_national_avg} ({obj.graduates_who_took_act_and_scored_above_national_avg_pct:.2f}%)"

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