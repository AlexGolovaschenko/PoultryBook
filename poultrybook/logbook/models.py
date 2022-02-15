from django.db import models

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
CNT_SERVICE_INSPECT	= 'SRV_INSPECT'	# осмотр оборудования
CNT_SERVICE_REPAIR	= 'SRV_REPAIR'	# ремонт оборудования
CNT_SERVICE_SETUP	= 'SRV_SETUP'	# настройка оборудования
CNT_SERVICE_REPLACE	= 'SRV_REPLACE'	# замена оборудования
CNT_VET_INSPECT		= 'VET_INSPECT'	# осмотр птицы
CNT_VET_VACCINATION	= 'VET_VACCIN'	# вакцинация птицы
CNT_VET_CURING		= 'VET_CURING'	# лечение птицы


class Room(models.Model):
	''' model with data about keeping room '''
	number = models.IntegerField(verbose_name='Номер помещения')
	
	def __str__(self):
		return f'Помещение {self.number}'

	class Meta:
		verbose_name = 'Помещение'
		verbose_name_plural = 'Помещения'


class Record(models.Model):
	room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name='Помещение')
	timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата')
	content_type = models.CharField(max_length=100, verbose_name='Тип записи')

	def __str__(self):
		return f'Запись {self.id}'

	class Meta:
		abstract = True


class IntegerRecord(Record):
	value = models.IntegerField(verbose_name='Значение')
	class Meta:
		verbose_name = 'Запись (integer)'
		verbose_name_plural = 'Записи (integer)'

class FloatRecord(Record):
	value = models.FloatField(verbose_name='Значение')
	class Meta:
		verbose_name = 'Запись (float)'
		verbose_name_plural = 'Записи (float)'

class TextRecord(Record):
	value = models.CharField(max_length=200, verbose_name='Значение')
	class Meta:
		verbose_name = 'Запись (text)'
		verbose_name_plural = 'Записи (text)'


CNT_CHOICES = [
	(CNT_BIRDS_NUMBER, 		'Entered birds number'),
	(CNT_BIRDS_DIED, 		'Entered birds died'),
	(CNT_BIRDS_APPEND, 		'Entered birds append'),
	(CNT_BIRDS_REMOVED, 	'Entered birds removed'),
	(CNT_BIRDS_WEIGHT, 		'Entered birds weight'),
	(CNT_BIRDS_UNIF, 		'Entered birds uniformity'),
	(CNT_CLIMAT_RTEMP, 		'Entered room temperature'),
	(CNT_CLIMAT_RHUM, 		'Entered room humidity'),
	(CNT_CLIMAT_CO2, 		'Entered CO2 concentration'),
	(CNT_CLIMAT_NH3, 		'Entered NH3 concentration'),
	(CNT_SERVICE_INSPECT, 	'Equipent ispection'),
	(CNT_SERVICE_REPAIR, 	'Equipment repair'),
	(CNT_SERVICE_SETUP, 	'Equipment setup'),
	(CNT_SERVICE_REPLACE, 	'Equipment replace'),
	(CNT_VET_INSPECT, 		'Poultry inspection'),
	(CNT_VET_VACCINATION, 	'Poultry vaccination'),
	(CNT_VET_CURING, 		'Poultry curing'),
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
	CNT_SERVICE_INSPECT	: TextRecord,
	CNT_SERVICE_REPAIR	: TextRecord,
	CNT_SERVICE_SETUP	: TextRecord,
	CNT_SERVICE_REPLACE	: TextRecord,
	CNT_VET_INSPECT		: TextRecord,
	CNT_VET_VACCINATION	: TextRecord,
	CNT_VET_CURING		: TextRecord,
	}


# class PoultryKeepingStatistics(models.Model):
# 	''' this model has functions for calculate actual values 
# 	of livestock in selected poultry house
# 	and append new records to statistics logbook '''

# 	def current_birds_number(self, room):
# 		return 0

# 	def current_birds_weight(self, room):
# 		return 0

# 	def add_new_record(self, room, content_type, value):
# 		record_model = RECORDS_TYPES(content_type)
# 		record_model(room= room, content_type= content_type, value= value)
# 		record_model.save()



