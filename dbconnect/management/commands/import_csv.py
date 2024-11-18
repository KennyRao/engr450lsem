import csv
from django.core.management.base import BaseCommand
from dbconnect.models import StlDistrict, StlDisciplineIncidents, StlDemographic, StlActScore, StlStudentStaffRatio

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **options):
        # Import StlDistrict
        self.import_stl_district('dbconnect/management/commands/csv_data/DESE STL Districts Names and Codes.csv')
        
        # Import StlDisciplineIncidents
        self.import_stl_discipline_incidents('dbconnect/management/commands/csv_data/DESE STL Districts Discipline Incidents Data.csv')
        
        # Import StlDemographic
        self.import_stl_demographic('dbconnect/management/commands/csv_data/DESE STL Districts Demographic Data.csv')
        
        # Import StlActScore
        self.import_stl_act_score('dbconnect/management/commands/csv_data/DESE STL Districts ACT Scores Data.csv')
        
        # Import StlStudentStaffRatio
        self.import_stl_student_staff_ratio('dbconnect/management/commands/csv_data/DESE STL Districts Student-Staff Ratio Data.csv')

    def import_stl_district(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StlDistrict.objects.create(
                    county_district_code=row['county_district_code'],
                    district_name=row['district_name']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported StlDistrict data'))

    def import_stl_discipline_incidents(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StlDisciplineIncidents.objects.create(
                    year=row['year'],
                    county_district_code=row['county_district_code'],
                    enrollment_grades_k_12=row['enrollment_grades_k_12'],
                    discipline_incidents=row['discipline_incidents'],
                    discipline_alcohol=row['discipline_alcohol'],
                    discipline_drug=row['discipline_drug'],
                    discipline_other=row['discipline_other'],
                    discipline_tobacco=row['discipline_tobacco'],
                    discipline_violence=row['discipline_violence'],
                    discipline_weapon=row['discipline_weapon'],
                    discipline_removal_in_schl_susp=row['discipline_removal_in_schl_susp'],
                    discipline_removal_out_schl_susp=row['discipline_removal_out_schl_susp'],
                    discipline_removal_expulsion=row['discipline_removal_expulsion'],
                    discipline_more_10_days=row['discipline_more_10_days']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported StlDisciplineIncidents data'))

    def import_stl_demographic(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StlDemographic.objects.create(
                    year=row['year'],
                    county_district_code=row['county_district_code'],
                    enrollment_grades_k_12=row['enrollment_grades_k_12'],
                    january_membership=row['january_membership'],
                    lunch_count_free_reduced=row['lunch_count_free_reduced'],
                    enrollment_asian=row['enrollment_asian'],
                    enrollment_asian_pacific_islander=row['enrollment_asian_pacific_islander'],
                    enrollment_black=row['enrollment_black'],
                    enrollment_hispanic=row['enrollment_hispanic'],
                    enrollment_indian=row['enrollment_indian'],
                    enrollment_multiracial=row['enrollment_multiracial'],
                    enrollment_pacific_islander=row['enrollment_pacific_islander'],
                    enrollment_white=row['enrollment_white'],
                    ell_lep_students_enrolled_k_12=row['ell_lep_students_enrolled_k_12'],
                    ell_lep_students_enrolled_pk=row['ell_lep_students_enrolled_pk'],
                    iep_schoolage_childcount=row['iep_schoolage_childcount']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported StlDemographic data'))

    def import_stl_act_score(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StlActScore.objects.create(
                    year=row['year'],
                    county_district_code=row['county_district_code'],
                    act_tests_administered=row['act_tests_administered'],
                    graduates=row['graduates'],
                    graduates_with_act_score_above_national_avg=row['graduates_with_act_score_above_national_avg'],
                    act_composite_score=row['act_composite_score'],
                    act_english_score=row['act_english_score'],
                    act_math_score=row['act_math_score'],
                    act_reading_score=row['act_reading_score'],
                    act_science_score=row['act_science_score']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported StlActScore data'))

    def import_stl_student_staff_ratio(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StlStudentStaffRatio.objects.create(
                    year=row['year'],
                    county_district_code=row['county_district_code'],
                    students_per_admin_ratio=row['students_per_admin_ratio'],
                    students_per_classrm_tch_ratio=row['students_per_classrm_tch_ratio'],
                    students_per_teacher_ratio=row['students_per_teacher_ratio']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported StlStudentStaffRatio data'))
