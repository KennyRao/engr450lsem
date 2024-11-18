MariaDB [lsem]> SHOW CREATE TABLE stl_district;
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table        | Create Table                                                                                                                                                                                                             |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stl_district | CREATE TABLE `stl_district` (
  `county_district_code` int(11) NOT NULL,
  `district_name` varchar(50) NOT NULL,
  PRIMARY KEY (`county_district_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

MariaDB [lsem]> SHOW CREATE TABLE stl_discipline_incidents;
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                    | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stl_discipline_incidents | CREATE TABLE `stl_discipline_incidents` (
  `year` int(11) NOT NULL,
  `county_district_code` int(11) NOT NULL,
  `enrollment_grades_k_12` int(11) NOT NULL,
  `discipline_incidents` int(11) NOT NULL,
  `discipline_incident_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_incidents` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_alcohol` int(11) NOT NULL,
  `discipline_alcohol_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_alcohol` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_drug` int(11) NOT NULL,
  `discipline_drug_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_drug` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_other` int(11) NOT NULL,
  `discipline_other_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_other` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_tobacco` int(11) NOT NULL,
  `discipline_tobacco_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_tobacco` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_violence` int(11) NOT NULL,
  `discipline_violence_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_violence` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_weapon` int(11) NOT NULL,
  `discipline_weapon_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_weapon` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_removal_in_schl_susp` int(11) NOT NULL,
  `discipline_removal_in_schl_susp_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_removal_in_schl_susp` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_removal_out_schl_susp` int(11) NOT NULL,
  `discipline_removal_out_schl_susp_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_removal_out_schl_susp` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_removal_expulsion` int(11) NOT NULL,
  `discipline_removal_expulsion_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_removal_expulsion` / `enrollment_grades_k_12` * 100) STORED,
  `discipline_more_10_days` int(11) NOT NULL,
  `discipline_more_10_days_rate` decimal(5,2) GENERATED ALWAYS AS (`discipline_more_10_days` / `enrollment_grades_k_12` * 100) STORED,
  PRIMARY KEY (`year`,`county_district_code`),
  KEY `discipline_fk1` (`county_district_code`),
  CONSTRAINT `discipline_fk1` FOREIGN KEY (`county_district_code`) REFERENCES `stl_district` (`county_district_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

MariaDB [lsem]> show create table stl_demographic;
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table           | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stl_demographic | CREATE TABLE `stl_demographic` (
  `year` int(11) NOT NULL,
  `county_district_code` int(11) NOT NULL,
  `enrollment_grades_k_12` int(11) NOT NULL,
  `january_membership` decimal(11,2) NOT NULL,
  `lunch_count_free_reduced` decimal(11,2) NOT NULL,
  `lunch_count_free_reduced_pct` decimal(5,2) GENERATED ALWAYS AS (`lunch_count_free_reduced` / `january_membership` * 100) STORED,
  `enrollment_asian` int(11) NOT NULL,
  `enrollment_asian_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_asian` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_asian_pacific_islander` int(11) NOT NULL,
  `enrollment_asian_pacific_islander_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_asian_pacific_islander` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_black` int(11) NOT NULL,
  `enrollment_black_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_black` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_hispanic` int(11) NOT NULL,
  `enrollment_hispanic_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_hispanic` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_indian` int(11) NOT NULL,
  `enrollment_indian_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_indian` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_multiracial` int(11) NOT NULL,
  `enrollment_multiracial_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_multiracial` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_pacific_islander` int(11) NOT NULL,
  `enrollment_pacific_islander_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_pacific_islander` / `enrollment_grades_k_12` * 100) STORED,
  `enrollment_white` int(11) NOT NULL,
  `enrollment_white_pct` decimal(5,2) GENERATED ALWAYS AS (`enrollment_white` / `enrollment_grades_k_12` * 100) STORED,
  `ell_lep_students_enrolled_k_12` int(11) NOT NULL,
  `ell_lep_students_enrolled_k_12_pct` decimal(5,2) GENERATED ALWAYS AS (`ell_lep_students_enrolled_k_12` / `enrollment_grades_k_12` * 100) STORED,
  `ell_lep_students_enrolled_pk` int(11) NOT NULL,
  `ell_lep_students_enrolled_pk_pct` decimal(5,2) GENERATED ALWAYS AS (`ell_lep_students_enrolled_pk` / `enrollment_grades_k_12` * 100) STORED,
  `iep_schoolage_childcount` int(11) NOT NULL,
  `iep_incidence_rate` decimal(5,2) GENERATED ALWAYS AS (`iep_schoolage_childcount` / `enrollment_grades_k_12` * 100) STORED,
  PRIMARY KEY (`year`,`county_district_code`),
  KEY `demographic_fk1` (`county_district_code`),
  CONSTRAINT `demographic_fk1` FOREIGN KEY (`county_district_code`) REFERENCES `stl_district` (`county_district_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

MariaDB [lsem]> show create table stl_act_score;
+---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table         | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stl_act_score | CREATE TABLE `stl_act_score` (
  `year` int(11) NOT NULL,
  `county_district_code` int(11) NOT NULL,
  `act_tests_administered` int(11) NOT NULL,
  `graduates` int(11) NOT NULL,
  `graduates_with_act_score_above_national_avg` int(11) NOT NULL,
  `graduates_with_act_score_above_national_avg_pct` decimal(5,2) GENERATED ALWAYS AS (`graduates_with_act_score_above_national_avg` / `graduates` * 100) STORED,
  `act_composite_score` decimal(3,1) NOT NULL,
  `act_english_score` decimal(3,1) NOT NULL,
  `act_math_score` decimal(3,1) NOT NULL,
  `act_reading_score` decimal(3,1) NOT NULL,
  `act_science_score` decimal(3,1) NOT NULL,
  `graduates_who_took_act_and_scored_above_national_avg_pct` decimal(5,2) GENERATED ALWAYS AS (`graduates_with_act_score_above_national_avg` / `act_tests_administered` * 100) STORED COMMENT 'graduates_who_took_act_and_scored_above_national_average_percent',
  PRIMARY KEY (`year`,`county_district_code`),
  KEY `act_score_fk1` (`county_district_code`),
  CONSTRAINT `act_score_fk1` FOREIGN KEY (`county_district_code`) REFERENCES `stl_district` (`county_district_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

MariaDB [lsem]> show create table stl_student_staff_ratio;
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                   | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stl_student_staff_ratio | CREATE TABLE `stl_student_staff_ratio` (
  `year` int(11) NOT NULL,
  `county_district_code` int(11) NOT NULL,
  `students_per_admin_ratio` int(11) NOT NULL,
  `students_per_classrm_tch_ratio` int(11) NOT NULL,
  `students_per_teacher_ratio` int(11) NOT NULL,
  PRIMARY KEY (`year`,`county_district_code`),
  KEY `student_staff_ratio_fk1` (`county_district_code`),
  CONSTRAINT `student_staff_ratio_fk1` FOREIGN KEY (`county_district_code`) REFERENCES `stl_district` (`county_district_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
