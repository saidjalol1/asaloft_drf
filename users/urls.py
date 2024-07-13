from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

app_name = "users_app"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]