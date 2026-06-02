from django.urls import path

from .views import workspace_create


urlpatterns = [
	path('', workspace_create),
]
