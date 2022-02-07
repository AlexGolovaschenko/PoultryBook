from django.db import models
from logbook.models import Room, IntegerRecord, FloatRecord 

CNT_BIRDS_NUMBER 	= 'BRD_BIRDS'	# количество птицы в птичнике
CNT_BIRDS_DIED 		= 'BRD_DIED'	# количество умершей птицы (падеж)
CNT_BIRDS_APPEND 	= 'BRD_APPEND' 	# количество добавленой птицы
CNT_BIRDS_REMOVED 	= 'BRD_REMOVED'	# количество изьятой птицы
CNT_BIRDS_WEIGHT 	= 'BRD_WEIGHT'	# средний вес птицы
CNT_BIRDS_UNIF 		= 'BRD_UNIF'	# значение однородности поголовья
CNT_CLIMAT_RTEMP 	= 'CLM_RTEMP'	# средняя температура в помещении
CNT_CLIMAT_RHUM 	= 'CLM_RHUM'	# влажность воздуха в помещении
CNT_CLIMAT_CO2 		= 'CLM_CO2'		# концентрация CO2 в помещении
CNT_CLIMAT_NH3 		= 'CLM_NH3'		# концентрация NH3 в помещении

CNT_CHOICES = [
	(CNT_BIRDS_NUMBER, 	'Entered birds number'),
	(CNT_BIRDS_DIED, 	'Entered birds died'),
	(CNT_BIRDS_APPEND, 	'Entered birds append'),
	(CNT_BIRDS_REMOVED, 'Entered birds removed'),
	(CNT_BIRDS_WEIGHT, 	'Entered birds weight'),
	(CNT_BIRDS_UNIF, 	'Entered birds uniformity'),
	(CNT_CLIMAT_RTEMP, 	'Entered room temperature'),
	(CNT_CLIMAT_RHUM, 	'Entered room humidity'),
	(CNT_CLIMAT_CO2, 	'Entered CO2 concentration'),
	(CNT_CLIMAT_NH3, 	'Entered NH3 concentration'),
	]

RECORDS_TYPES = {
	CNT_BIRDS_NUMBER 	: IntegerRecord,
	CNT_BIRDS_DIED 		: IntegerRecord,
	CNT_BIRDS_APPEND 	: IntegerRecord,
	CNT_BIRDS_REMOVED 	: IntegerRecord,
	CNT_BIRDS_WEIGHT 	: FloatRecord,
	CNT_BIRDS_UNIF 		: FloatRecord,
	CNT_CLIMAT_RTEMP 	: FloatRecord,
	CNT_CLIMAT_RHUM 	: FloatRecord,
	CNT_CLIMAT_CO2 		: FloatRecord,
	CNT_CLIMAT_NH3 		: FloatRecord,
	}


class PoultryKeepingStatistics(models.Model):
	''' this model has functions for calculate actual values 
	of livestock in selected poultry house
	and append new records to statistics logbook '''

	def current_birds_number(self, room):
		return 0

	def current_birds_weight(self, room):
		return 0

	def add_new_record(self, room, content_type, value):
		record_model = RECORDS_TYPES(content_type)
		record_model(room= room, content_type= content_type, value= value)
		record_model.save()


