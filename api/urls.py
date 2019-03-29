from django.urls import path, include
from rest_framework import routers 
from .views_api import price_views, tenant_views, user_views, rate_views

router = routers.DefaultRouter()
router.register('tenant', tenant_views.TenantViewSet)
router.register('user', user_views.UserView)
router.register('price', price_views.PriceView)

router.register('rate', rate_views.RateView)

urlpatterns = [
   path('v1/', include(router.urls)),
]