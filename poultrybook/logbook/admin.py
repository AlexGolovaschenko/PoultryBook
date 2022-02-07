from django.contrib import admin
from .models import Room, IntegerRecord, FloatRecord, TextRecord

admin.site.register(Room)
admin.site.register(IntegerRecord)
admin.site.register(FloatRecord)
admin.site.register(TextRecord)
