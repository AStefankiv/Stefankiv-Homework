from django.http import JsonResponse
from .models import Purchase

def purchases_view(request):
    purchases = Purchase.objects.all()
    data = [{"id": purchase.id, "product_name": purchase.product_name, "price": purchase.price, "purchase_date": purchase.purchase_date} for purchase in purchases]
    return JsonResponse(data, safe=False)