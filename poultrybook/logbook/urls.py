from django.urls import path
from .views import workspace_view, rooms_list_view, record_detail_view, log_view, home_view


app_name = 'logbook'

urlpatterns = [
	path('', home_view, name='home'),
	path('room/select', rooms_list_view, name='rooms_list'),
	path('room/<int:room_number>', workspace_view, name='workspace'),
	path('room/<int:room_number>/records/<str:record_type>', record_detail_view, name='record'),
	path('log', log_view, name='log')
]