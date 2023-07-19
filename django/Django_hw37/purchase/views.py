from django.http import JsonResponse
from .models import Purchase

def purchase_list_json(request):
    # Get all purchases from the database
    purchases = Purchase.objects.all()

    # Serialize the queryset into JSON format
    purchases_json = [{"user": purchase.user.username, "book": purchase.book.title, "price": purchase.price} for purchase in purchases]

    # Return the JSON response
    return JsonResponse(purchases_json, safe=False)