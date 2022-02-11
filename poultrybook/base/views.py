from django.shortcuts import render

from poultry_statistics.views import handle_form
from poultry_statistics.models import ( 
	CNT_BIRDS_NUMBER, CNT_BIRDS_DIED, CNT_BIRDS_APPEND,
	CNT_BIRDS_REMOVED, CNT_BIRDS_WEIGHT, CNT_BIRDS_UNIF,
	CNT_CLIMAT_RTEMP, CNT_CLIMAT_RHUM, CNT_CLIMAT_CO2,
	CNT_CLIMAT_NH3 )



def home_view(request):
	birds_number_form = handle_form(request, CNT_BIRDS_NUMBER)
	context = {
		'room': 13,
		'birds_number_form': birds_number_form
	}
	return render(request, 'base/home.html', context)