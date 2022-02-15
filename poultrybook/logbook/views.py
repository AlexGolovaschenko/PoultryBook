from django.shortcuts import render

from .models import RECORDS_TYPES, IntegerRecord, FloatRecord, TextRecord
from .forms import IntegerRecordForm, FloatRecordForm, TextRecordForm



def handle_form(request, content_type):
	FormClass = get_form_class(content_type)
	form = FormClass(request.POST or None)
	if form.is_valid() and (form.cleaned_data['content_type'] == content_type):
		print(f'Entered value of {content_type} is: ', form.cleaned_data['value'])
		return form
	else:
		return FormClass(initial={'content_type': content_type})


def get_form_class(content_type):
	if RECORDS_TYPES[content_type] == IntegerRecord:
		return IntegerRecordForm
	elif RECORDS_TYPES[content_type] == FloatRecord:
		return FloatRecordForm
	elif RECORDS_TYPES[content_type] == TextRecord:
		return TextRecordForm
	else:
		raise Exception('Record dtype does not supported')




