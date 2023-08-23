from django_filters import rest_framework as filters
from django.db.models import Q

from products.models import Product


class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='category__title', lookup_expr='icontains')
    brand = filters.CharFilter(
        field_name='brand__title', lookup_expr='icontains')
    colors = filters.CharFilter(
        field_name='colors__title', lookup_expr='icontains')
    size = filters.CharFilter(field_name='dimensions__title',
                              lookup_expr='icontains')
    search = filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) |
                               Q(description__icontains=value))

    class Meta:
        model = Product
        fields = ['category', 'brand', 'colors', 'size', 'search']
