from rest_framework.routers import DefaultRouter
from orders.api.v1.view import OrderView

router = DefaultRouter()
router.register(r'order', OrderView, basename='order')

app_name = 'order'
urlpatterns = router.urls
