import imp
from rest_framework import filters
from rest_framework import viewsets
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id","title"]
    filterset_fields = ["is_active", "price"]
    ordering_fields = ["amount", "price"]


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "title"]
