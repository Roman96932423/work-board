from django.urls import path

from .views import create_board, board_detail


urlpatterns = [
	path('', create_board),
	path('<int:board_id>/', board_detail)
]
