from django.urls import path
from .views import workspace_view, record_detail_view, log_view


app_name = 'logbook'

urlpatterns = [
	path('', workspace_view, name='workspace'),
	path('records/<str:record_type>', record_detail_view, name='record'),
	path('log', log_view, name='log')
]