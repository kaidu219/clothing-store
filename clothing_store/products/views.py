from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny, IsAdminUser
)

from products.models import Product
from products.serializers import ProductSerializer, ProductDetailSerializer
from products.filters import ProductFilter


class ProductsView(viewsets.ModelViewSet):
    """
    Класс предсттавляет список товаров, при детальном и при полном отображении
    применяются разные сериалайзеры, так же при разных методах применяется 
    разные уровни доступа.
    """
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return ProductDetailSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            return [IsAdminUser()]
        return [AllowAny()]
