from django.db import models

# Create your models here.

class StlDistrict(models.Model):
    county_district_code = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'stl_district'  # Specify the existing table name

    def __str__(self):
        return self.district_name

class StlDisciplineIncidents(models.Model):
    year = models.IntegerField()
    county_district_code = models.ForeignKey('StlDistrict', on_delete=models.CASCADE, to_field='county_district_code')
    enrollment_grades_k_12 = models.IntegerField()
    discipline_incidents = models.IntegerField()
    discipline_alcohol = models.IntegerField()
    discipline_drug = models.IntegerField()
    discipline_other = models.IntegerField()
    discipline_tobacco = models.IntegerField()
    discipline_violence = models.IntegerField()
    discipline_weapon = models.IntegerField()
    discipline_removal_in_schl_susp = models.IntegerField()
    discipline_removal_out_schl_susp = models.IntegerField()
    discipline_removal_expulsion = models.IntegerField()
    discipline_more_10_days = models.IntegerField()

    class Meta:
        db_table = 'stl_discipline_incidents'
        unique_together = ('year', 'county_district_code')

    @property
    def discipline_incident_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_incidents / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_alcohol_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_alcohol / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_drug_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_drug / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_other_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_other / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_tobacco_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_tobacco / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_violence_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_violence / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_weapon_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_weapon / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_removal_in_schl_susp_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_removal_in_schl_susp / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_removal_out_schl_susp_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_removal_out_schl_susp / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_removal_expulsion_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_removal_expulsion / self.enrollment_grades_k_12) * 100
        return None

    @property
    def discipline_more_10_days_rate(self):
        if self.enrollment_grades_k_12:
            return (self.discipline_more_10_days / self.enrollment_grades_k_12) * 100
        return None

class StlDemographic(models.Model):
    year = models.IntegerField()
    county_district_code = models.ForeignKey('StlDistrict', on_delete=models.CASCADE, to_field='county_district_code')
    enrollment_grades_k_12 = models.IntegerField()
    january_membership = models.DecimalField(max_digits=11, decimal_places=2)
    lunch_count_free_reduced = models.DecimalField(max_digits=11, decimal_places=2)
    enrollment_asian = models.IntegerField()
    enrollment_asian_pacific_islander = models.IntegerField()
    enrollment_black = models.IntegerField()
    enrollment_hispanic = models.IntegerField()
    enrollment_indian = models.IntegerField()
    enrollment_multiracial = models.IntegerField()
    enrollment_pacific_islander = models.IntegerField()
    enrollment_white = models.IntegerField()
    ell_lep_students_enrolled_k_12 = models.IntegerField()
    ell_lep_students_enrolled_pk = models.IntegerField()
    iep_schoolage_childcount = models.IntegerField()

    class Meta:
        db_table = 'stl_demographic'
        unique_together = ('year', 'county_district_code')

    @property
    def lunch_count_free_reduced_pct(self):
        return (self.lunch_count_free_reduced / self.january_membership) * 100 if self.january_membership != 0 else 0

    @property
    def enrollment_asian_pct(self):
        return (self.enrollment_asian / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_asian_pacific_islander_pct(self):
        return (self.enrollment_asian_pacific_islander / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_black_pct(self):
        return (self.enrollment_black / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_hispanic_pct(self):
        return (self.enrollment_hispanic / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_indian_pct(self):
        return (self.enrollment_indian / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_multiracial_pct(self):
        return (self.enrollment_multiracial / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_pacific_islander_pct(self):
        return (self.enrollment_pacific_islander / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def enrollment_white_pct(self):
        return (self.enrollment_white / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def ell_lep_students_enrolled_k_12_pct(self):
        return (self.ell_lep_students_enrolled_k_12 / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def ell_lep_students_enrolled_pk_pct(self):
        return (self.ell_lep_students_enrolled_pk / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

    @property
    def iep_incidence_rate(self):
        return (self.iep_schoolage_childcount / self.enrollment_grades_k_12) * 100 if self.enrollment_grades_k_12 != 0 else 0

class StlActScore(models.Model):
    year = models.IntegerField()
    county_district_code = models.ForeignKey('StlDistrict', on_delete=models.CASCADE, to_field='county_district_code')
    act_tests_administered = models.IntegerField()
    graduates = models.IntegerField()
    graduates_with_act_score_above_national_avg = models.IntegerField()
    act_composite_score = models.DecimalField(max_digits=3, decimal_places=1)
    act_english_score = models.DecimalField(max_digits=3, decimal_places=1)
    act_math_score = models.DecimalField(max_digits=3, decimal_places=1)
    act_reading_score = models.DecimalField(max_digits=3, decimal_places=1)
    act_science_score = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        db_table = 'stl_act_score'
        unique_together = ('year', 'county_district_code')

    @property
    def graduates_with_act_score_above_national_avg_pct(self):
        return (self.graduates_with_act_score_above_national_avg / self.graduates) * 100 if self.graduates != 0 else 0

    @property
    def graduates_who_took_act_and_scored_above_national_avg_pct(self):
        return (self.graduates_with_act_score_above_national_avg / self.act_tests_administered) * 100 if self.act_tests_administered != 0 else 0

class StlStudentStaffRatio(models.Model):
    year = models.IntegerField()
    county_district_code = models.ForeignKey('StlDistrict', on_delete=models.CASCADE, to_field='county_district_code')
    students_per_admin_ratio = models.IntegerField()
    students_per_classrm_tch_ratio = models.IntegerField()
    students_per_teacher_ratio = models.IntegerField()

    class Meta:
        db_table = 'stl_student_staff_ratio'
        unique_together = ('year', 'county_district_code')


