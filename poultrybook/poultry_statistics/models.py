from django.db import models
from logbook.models import Room, IntegerRecord, FloatRecord 

CNT_BIRDS_NUMBER = 'BIRDS'
CNT_BIRDS_DIED = 'DIED'
CNT_BIRDS_APPEND = 'APPEND'

CNT_CHOICES = (
	(CNT_BIRDS_NUMBER, 'entered_birds_number'),
	(CNT_BIRDS_DIED, 'entered_birds_died'),
	(CNT_BIRDS_APPEND, 'entered_birds_append'),
	)

RECORDS_TYPES = {
	CNT_BIRDS_NUMBER: IntegerRecord,
	CNT_BIRDS_DIED: IntegerRecord,
	CNT_BIRDS_APPEND: IntegerRecord,
	}

class PoultryStatistics(models.Model):
	''' this model has functions for calculate actual values 
	of livestock in selected poultry house '''

	def current_birds_number(self, room):
		return 0

	def current_birds_weight(self, room):
		return 0

	def add_new_record(self, room, content_type, value):
		record_model = RECORDS_TYPES(content_type)
		record_model(room= room, content_type= content_type, value= value)
		record_model.save()

# class PoultryStatistics(models.Model):
# 	entered_birds_number = models.IntegerField()
# 	entered_birds_died = models.IntegerField()
# 	entered_birds_append = models.IntegerField()
# 	entered_birds_removed = models.IntegerField()
# 	entered_birds_weight = models.FloatField()
# 	entered_birds_uniformity = models.FloatField()
# 	def get_current_birds_number(self):
# 		pass
# 	def get_current_birds_weight(self):
# 		pass

# class ClimatStatistics(models.Model):
# 	entered_room_temperature = models.FloatField()
# 	entered_room_humidity = models.FloatField()
# 	entered_CO2_level = models.FloatField()
# 	entered_NH3_level = models.FloatField()
