from django.shortcuts import render

from .models import ( 
	CNT_BIRDS_NUMBER, CNT_BIRDS_DIED, CNT_BIRDS_APPEND,
	CNT_BIRDS_REMOVED, CNT_BIRDS_WEIGHT, CNT_BIRDS_UNIF,
	CNT_CLIMAT_RTEMP, CNT_CLIMAT_RHUM, CNT_CLIMAT_CO2,
	CNT_CLIMAT_NH3 )

from .models import RECORDS_TYPES, IntegerRecord, FloatRecord

from .forms import IntegerRecordForm, FloatRecordForm



def handle_form(request, content_type):
	FormClass = get_form_class(content_type)
	if request.method == "POST":
		form = FormClass(request.POST)
		if form.is_valid():
			print(f'value of {content_type} is: ', form.cleaned_data['value'])
			pass
	else:
		form = FormClass()

	return form



def get_form_class(content_type):
	if RECORDS_TYPES[content_type] == IntegerRecord:
		return IntegerRecordForm
	elif RECORDS_TYPES[content_type] == FloatRecord:
		return FloatRecordForm
	else:
		raise Exception('Record dtype does not supported')




