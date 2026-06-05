from django.urls import path

from .views import workspace_list_create, workspace_detail_update_delete


urlpatterns = [
	path('', workspace_list_create),
	path('<int:ws_id>/', workspace_detail_update_delete)
]
