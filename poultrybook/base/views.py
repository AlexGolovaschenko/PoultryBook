from django.shortcuts import render

def home_view(request):
	context = {
		'room': 13,

	}
	return render(request, 'base/home.html', context)