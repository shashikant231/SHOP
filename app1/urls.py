from django.urls import path, include
from app1 import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shop_api', views.ShopViewSet,basename='shop_api'),
router.register('product_api',views.ProductViewSet, basename='product_api')
router.register('category_api',views.CategoryViewSet, basename='category_api')

urlpatterns = [
    path('',include(router.urls)),

]