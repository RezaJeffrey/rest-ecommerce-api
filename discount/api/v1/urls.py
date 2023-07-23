from rest_framework.routers import DefaultRouter
from .views import DiscountCodeViewSet

router = DefaultRouter()
router.register(r"discount_code", DiscountCodeViewSet, basename="discount_code")

app_name = "discount"

urlpatterns = router.urls



