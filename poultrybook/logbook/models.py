from django.db import models


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
	value = models.CharField(max_length=400, verbose_name='Значение')
	class Meta:
		verbose_name = 'Запись (text)'
		verbose_name_plural = 'Записи (text)'




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



