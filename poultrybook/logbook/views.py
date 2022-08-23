from django.shortcuts import render, redirect

from . import configs
from .models import Room
from .utils import get_datatype_model, get_datatype_form


def workspace_view(request):
	context = {
		'room': 13,
		'birds_workspace_items': configs.BIRDS_WORKSPACE_CONFIG,
		'climat_workspace_items': configs.CLIMAT_WORKSPACE_CONFIG,
		'service_workspace_items': configs.SERVICE_WORKSPACE_CONFIG,
		'vet_workspace_items': configs.VET_WORKSPACE_CONFIG,
	}
	return render(request, 'logbook/workspace.html', context)


def log_view(request):
	room_number = 1
	room = Room.objects.get(number=room_number)
	context = {'records': []}
	for record in room.records_list():
		context['records'].append(record.log_message())
	return render(request, 'logbook/logslist.html', context)


def record_detail_view(request, record_type):
	next_page='logbook:workspace'
	try:
		context = configs.RECORDS_CONFIG[record_type]
		context['form'], submit_success = handle_form(request, record_type)
		if submit_success: 
			return redirect(next_page)
	except Exception as e:
		context = {}
	return render(request, 'logbook/record_detail.html', context)


def handle_form(request, content_type):
	if not content_type:
		return None
	FormClass = get_datatype_form(content_type)
	form = FormClass(request.POST or None)
	if form.is_valid() and (form.cleaned_data['content_type'] == content_type):
		print(f'Entered value of {content_type} is: ', form.cleaned_data['value'])
		save_form_data(form.cleaned_data)
		return form, form.is_valid()
	else:
		return FormClass(initial={'content_type': content_type}), False


def save_form_data(cleaned_data):
	content_type = cleaned_data['content_type']
	room = Room.objects.first()
	Model = get_datatype_model(content_type)
	new_record = Model(room=room, content_type=content_type, value=cleaned_data['value'])
	new_record.save()
