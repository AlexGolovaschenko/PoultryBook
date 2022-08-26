from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import configs
from .models import Room
from .utils import get_datatype_model, get_datatype_form
from .forms import RecordDemoForm


@login_required
def home_view(request):
	return redirect('logbook:rooms_list')


@login_required
def workspace_view(request, room_number):
	context = {
		'room': room_number,
		'birds_workspace_items': configs.BIRDS_WORKSPACE_CONFIG,
		'climat_workspace_items': configs.CLIMAT_WORKSPACE_CONFIG,
		'service_workspace_items': configs.SERVICE_WORKSPACE_CONFIG,
		'vet_workspace_items': configs.VET_WORKSPACE_CONFIG,
	}
	return render(request, 'logbook/workspace.html', context)


@login_required
def rooms_list_view(request):
	rooms = Room.objects.all()
	return render(request, 'logbook/rooms_list.html', {'rooms':rooms})


@login_required
def log_view(request):
	all_rooms = Room.objects.all()
	context = {'records': []}
	for room in all_rooms:
		for record in room.records_list(sorted=False):
			context['records'].append(record.log_message())
	context['records'].sort(key=lambda x: x['timestamp'], reverse=True)
	return render(request, 'logbook/logslist.html', context)


@login_required
def record_detail_view(request, room_number, record_type):
	try:
		context = configs.RECORDS_CONFIG[record_type]
		context['room'] = room_number
		context['form'], submit_success = handle_form(request, room_number, record_type)
		if submit_success: 
			return redirect('logbook:workspace', room_number=room_number)
	except Exception as e:
		print(e)
		context = {'room':room_number}
	return render(request, 'logbook/record_detail.html', context)


def handle_form(request, room_number, content_type):
	if not content_type:
		return None
	FormClass = get_datatype_form(content_type)
	form = FormClass(request.POST or None)
	if form.is_valid() and (form.cleaned_data['content_type'] == content_type):
		print(f'Entered value of {content_type} is: ', form.cleaned_data['value'])
		save_form_data(room_number, form.cleaned_data)
		return form, form.is_valid()
	else:
		return FormClass(initial={'content_type': content_type}), False


def save_form_data(room_number, cleaned_data):
	content_type = cleaned_data['content_type']
	room = Room.objects.get(number=room_number)
	Model = get_datatype_model(content_type)
	new_record = Model(room=room, content_type=content_type, value=cleaned_data['value'])
	new_record.save()


@login_required
def demo_form_view(request):
	context={'form': RecordDemoForm()}
	return render(request, 'logbook/record_demo_form.html', context)