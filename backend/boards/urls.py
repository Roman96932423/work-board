from django.urls import path

from .views import boards_list_create, board_detail_update_delete


urlpatterns = [
	path('', boards_list_create),
	path('<int:board_id>/', board_detail_update_delete),
]
