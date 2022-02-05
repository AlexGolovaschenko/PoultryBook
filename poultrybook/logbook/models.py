from django.db import models


class Room(model.Models):
	''' model with data about keeping room '''
	mumber = models.IntegerField()


class Record(model.Models):
	room = models.ForeignKeyField(model = Room)
	timestamp = models.DateTimeField()
	content_type = models.CharField()

	class Meta:
		abstract = True


class IntegerRecord(Record):
	value = models.IntegerField()

class FloatRecord(Record):
	value = models.FloatField()

class TextRecord(Record):
	value = models.CharField()
