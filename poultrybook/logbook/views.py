from django.shortcuts import render

from . import configs
from .models import IntegerRecord, FloatRecord, TextRecord, Room
from .forms import IntegerRecordForm, FloatRecordForm, TextRecordForm


def workspace_view(request):
	context = {
		'room': 13,
		'birds_workspace_items': configs.BIRDS_WORKSPACE_CONFIG,
		'climat_workspace_items': configs.CLIMAT_WORKSPACE_CONFIG,
		'service_workspace_items': configs.SERVICE_WORKSPACE_CONFIG,
		'vet_workspace_items': configs.VET_WORKSPACE_CONFIG,
	}
	return render(request, 'logbook/workspace.html', context)


def record_detail_view(request, record_type):
	try:
		context = configs.RECORDS_CONFIG[record_type]
		context['form'] = handle_form(request, record_type)
	except:
		context = {}
	return render(request, 'logbook/record_detail.html', context)


def handle_form(request, content_type):
	if not content_type:
		return None

	FormClass = get_form_class(content_type)
	form = FormClass(request.POST or None)
	if form.is_valid() and (form.cleaned_data['content_type'] == content_type):
		print(f'Entered value of {content_type} is: ', form.cleaned_data['value'])
		save_form_data(form.cleaned_data)
		return form
	else:
		return FormClass(initial={'content_type': content_type})


def get_form_class(content_type):
	if configs.RECORDS_TYPES[content_type] == IntegerRecord:
		return IntegerRecordForm
	elif configs.RECORDS_TYPES[content_type] == FloatRecord:
		return FloatRecordForm
	elif configs.RECORDS_TYPES[content_type] == TextRecord:
		return TextRecordForm
	else:
		raise Exception('Record dtype does not supported')


def save_form_data(cleaned_data):
	content_type = cleaned_data['content_type']
	room = Room.objects.first()
	Model = configs.RECORDS_TYPES[content_type]
	new_record = Model(room=room, content_type=content_type, value=cleaned_data['value'])
	new_record.save()
