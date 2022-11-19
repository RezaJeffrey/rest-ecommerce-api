from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/api/v1/', include('users.api.v1.urls', namespace='v1')),
    path('categories/api/v1/', include('category.api.v1.urls', namespace='v1')),
    path('products/api/v1/', include('products.api.v1.urls', namespace='v1')),
    path('comments/api/v1/', include('comments.api.v1.urls', namespace='v1')),
    path('packs/api/v1/', include('productpacks.api.v1.urls', namespace='v1')),
    path('extra_fields/api/v1/', include('extra_fields.api.v1.urls', namespace='v1')),
    path('brands/api/v1/', include('brands.api.v1.urls', namespace='v1')),
    path('shops/api/v1/', include('shops.api.v1.urls', namespace='v1')),
    path('carts/api/v1/', include('carts.api.v1.urls', namespace='v1')),
    path('address/api/v1/', include('address.api.v1.urls', namespace='v1'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

