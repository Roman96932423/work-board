from django.urls import path

from .views import workspace_list_create, workspace_detail


urlpatterns = [
	path('', workspace_list_create),
	path('<int:ws_id>/', workspace_detail)
]
