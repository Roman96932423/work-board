from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


@api_view(['GET'])
def test_api(request):
    return Response({'message': 'API works'})


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/test/', test_api),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/users/', include('users.urls')),
    path('api/boards/', include('boards.urls')),
    # path('api/tasks/', include('tasks.urls'))
]
