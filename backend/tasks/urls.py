from django.urls import path

from .views import task_detail


urlpatterns = [
	path('<int:task_id>/', task_detail),
]
