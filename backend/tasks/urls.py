from django.urls import path

from .views import task_detail_update


urlpatterns = [
	path('<int:task_id>/', task_detail_update),
]
