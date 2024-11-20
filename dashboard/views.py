from django.shortcuts import render

# Create your views here.

FEATURE_MAP = {
    # StlDisciplineIncidents features
    'incident_rate': 'discipline_incident_rate',
    'in_school_susp_rate': 'discipline_removal_in_schl_susp_rate',
    'out_school_susp_rate': 'discipline_removal_out_schl_susp_rate',
    'expulsion_rate': 'discipline_removal_expulsion_rate',
    'more_than_10_days_rate': 'discipline_more_10_days_rate',

    # StlDemographic features
    'enrollment_asian_pct': 'enrollment_asian_pct',
    'enrollment_black_pct': 'enrollment_black_pct',
    'enrollment_hispanic_pct': 'enrollment_hispanic_pct',
    'enrollment_indian_pct': 'enrollment_indian_pct',
    'enrollment_multiracial_pct': 'enrollment_multiracial_pct',
    'enrollment_pacific_islander_pct': 'enrollment_pacific_islander_pct',
    'enrollment_white_pct': 'enrollment_white_pct',
    'free_lunch_pct': 'lunch_count_free_reduced_pct',
    'ell_k_12_pct': 'ell_lep_students_enrolled_k_12_pct',
    'ell_pk_pct': 'ell_lep_students_enrolled_pk_pct',
    'iep_rate': 'iep_incidence_rate',

    # StlActScore features
    'act_composite': 'act_composite_score',
    'act_english': 'act_english_score',
    'act_math': 'act_math_score',
    'act_reading': 'act_reading_score',
    'act_science': 'act_science_score',
    'graduates_above_national_avg_pct': 'graduates_with_act_score_above_national_avg_pct',
    'graduates_took_act_above_avg_pct': 'graduates_who_took_act_and_scored_above_national_avg_pct',

    # StlStudentStaffRatio features
    'student_teacher_ratio': 'students_per_teacher_ratio',
    'student_admin_ratio': 'students_per_admin_ratio',
    'student_classroom_teacher_ratio': 'students_per_classrm_tch_ratio',
}


def generate_dashboard(request):
    #extract the user's selected features from the submitted request
    features = request.GET.getlist('features') #ex: ['incident_rate', 'act_composite']

    #validate the selected features