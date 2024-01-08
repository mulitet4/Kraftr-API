from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('src.products.urls')),
    path('api/v1/user/', include('src.users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
