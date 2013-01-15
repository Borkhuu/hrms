from django.db import models
import datetime
from django.utils import timezone

class Hrm_education(models.Model):
	school = models.CharField(max_length=100)
	diplom_No = models.CharField(max_length=50)
	professionDesc = models.CharField(max_length=100)
	dateFrom = models.DateField()
	dateTo = models.DateField()
	registr = models.CharField(max_length=50)

class Dic_position_time(models.Model):
	position_time = models.IntegerField()
	position_info = models.CharField(max_length=30)
	
class Dic_position_type(models.Model):
	position_type = models.CharField(max_length=100)
	position_salary = models.CharField(max_length=30)
	
class Dic_country(models.Model):
	country_name = models.CharField(max_length=30)
	
class Dic_aimag(models.Model):
	aimag_name = models.CharField(max_length=30)
	country_id = models.ForeignKey(Dic_country)
	
class Dic_division(models.Model):
	division_name = models.CharField(max_length=200)
	division_phone = models.IntegerField()
			
class Dic_nationality(models.Model):
	nationality_info = models.CharField(max_length=50)
	
class Hrm_office_skill(models.Model):
	registr = models.CharField(max_length=20)
	office_skill_other = models.CharField(max_length=50)
	office_skill_rate = models.IntegerField()
	
class Hrm_skill(models.Model):
	registr = models.CharField(max_length=20)
	skill_rate = models.IntegerField()
	skill_other = models.CharField(max_length=50)
	skill_other_rate = models.IntegerField()
	
class Hrm_position(models.Model):
	position_name = models.CharField(max_length=255)
	division_id = models.ForeignKey(Dic_division)
	position_time_id = models.ForeignKey(Dic_position_time)
	position_type_id = models.ForeignKey(Dic_position_type)
	
class Dic_education(models.Model):
	education_id = models.ForeignKey(Hrm_education)
	education_info = models.CharField(max_length=255)

class Dic_skill(models.Model):
	skill_id = models.ForeignKey(Hrm_skill)
	skill_info = models.CharField(max_length=50)
	
class Dic_relation(models.Model):
	relation_info = models.CharField(max_length=50)
	
class Hrm_main(models.Model):
	registr = models.CharField(max_length=20)
	ovog = models.CharField(max_length=60)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	birthDate = models.DateField()
	Sex = models.CharField(max_length=20)
	sum_id = models.IntegerField()
	garal_id = models.IntegerField()
	soldier_id = models.IntegerField()
	home_address = models.TextField()
	phone = models.IntegerField()
	email = models.CharField(max_length=100)
	picture = models.CharField(max_length=250)
	postbox = models.CharField(max_length=200)
	birthArea = models.CharField(max_length=244)
	nationality_id = models.ForeignKey(Dic_nationality)
	userName = models.CharField(max_length=100)
	userPass = models.CharField(max_length=100)
	position_id = models.ForeignKey(Hrm_position)
	status = models.CharField(max_length=20)

class Dic_office_skill(models.Model):
	office_skill_id = models.ForeignKey(Hrm_office_skill)
	office_skill_info = models.CharField(max_length=100)
	
class Dic_sum(models.Model):
	aimag_id = models.ForeignKey(Dic_aimag)
	sum_name = models.CharField(max_length=30)
	
class Hrm_family(models.Model):
	registr = models.CharField(max_length=20)
	relation_id = models.IntegerField()
	fisrt_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_date = models.DateField()
	current_job = models.CharField(max_length=200)
	phone = models.IntegerField()
	sum_id = models.ForeignKey(Dic_sum)
	state = models.CharField(max_length=50)
	
class Dic_degree(models.Model):
	degree_info = models.CharField(max_length=100)

class Dic_garal(models.Model):
	garal_info = models.CharField(max_length=50)
	
class Dic_soldier(models.Model):
	soldier_info = models.CharField(max_length=50)

class Hrm_experience(models.Model):
	registr = models.CharField(max_length=20)
	where = models.CharField(max_length=255)
	position = models.CharField(max_length=100)
	dateFrom = models.DateField()
	dateTo = models.DateField()
	
class Dic_language(models.Model):
	language_info = models.CharField(max_length=100)

class Hrm_language(models.Model):
	registr = models.CharField(max_length=20)
	language_id = models.ForeignKey(Dic_language)
	language_listen = models.CharField(max_length=30)
	language_write = models.CharField(max_length=30)
	language_read = models.CharField(max_length=30)
	language_understand = models.CharField(max_length=30)
	
class Dic_command(models.Model):
	command_type = models.CharField(max_length=50)
	command_info = models.TextField()

class Hrm_command_employee(models.Model):
	command_no = models.IntegerField()
	registr = models.CharField(max_length=20)

class Hrm_command(models.Model):
	command_no = models.IntegerField()
	command_date = models.DateField()
	command_type = models.CharField(max_length=100)
	command_length = models.IntegerField()
	command_add = models.CharField(max_length=20)
	command_id = models.ForeignKey(Dic_command)

class Hrm_mergeshil(models.Model):
	registr = models.CharField(max_length=20)
	country_id = models.ForeignKey(Dic_country)
	where = models.CharField(max_length=30)
	date_start = models.DateField()
	date_end = models.DateField()
	direction = models.CharField(max_length=30)
	date_get_certificate = models.DateField()
