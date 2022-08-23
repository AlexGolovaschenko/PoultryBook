from django.shortcuts import render

def docs_view(request):
    return render(request, 'base/docs.html', {})