import django_filters
from .models import Purchase

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'product_name': ['exact', 'icontains'],
            'price': ['exact', 'gte', 'lte'],
            'purchase_date': ['exact', 'year__gt', 'year__lt'],
            'quantity': ['exact', 'gte', 'lte'],
        }
