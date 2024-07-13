from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace="users_app")),
    path('shop/', include('shop.urls', namespace="shop_app")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
