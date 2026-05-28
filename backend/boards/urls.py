from django.urls import path

from .views import create_board


urlpatterns = [
	path('', create_board),
]
