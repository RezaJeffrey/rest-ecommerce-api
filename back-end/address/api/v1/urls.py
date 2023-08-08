from rest_framework.routers import DefaultRouter
from address.api.v1.view import AddressView


router = DefaultRouter()
router.register(r'address', AddressView, basename='address')

app_name = 'address'
urlpatterns = router.urls
