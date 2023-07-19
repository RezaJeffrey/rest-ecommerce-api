from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Third-party
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Local
    path('admin/', admin.site.urls),
    path('shops/api/v1/', include('shops.api.v1.urls', namespace='v1')),
    path('users/api/v1/', include('users.api.v1.urls', namespace='users')),
    path('categories/api/v1/', include('category.api.v1.urls', namespace='v1')),
    path('products/api/v1/', include('products.api.v1.urls', namespace='v1')),
    path('comments/api/v1/', include('comments.api.v1.urls', namespace='v1')),
    path('packs/api/v1/', include('productpacks.api.v1.urls', namespace='v1')),
    path('extra_fields/api/v1/', include('extra_fields.api.v1.urls', namespace='v1')),
    path('brands/api/v1/', include('brands.api.v1.urls', namespace='v1')),
    path('carts/api/v1/', include('carts.api.v1.urls', namespace='v1')),
    path('address/api/v1/', include('address.api.v1.urls', namespace='v1')),
    path('orders/api/v1/', include('orders.api.v1.urls', namespace='v1')),
    #path('discounts/api/v1/', include('discount.api.v1.urls', namespace='v1')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
