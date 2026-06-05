from django.urls import path

from .views import workspace_list_create


urlpatterns = [
	path('', workspace_list_create),
]
