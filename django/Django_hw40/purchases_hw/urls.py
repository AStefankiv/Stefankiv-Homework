from django.urls import path
from .views import PurchasesView, PurchaseDetailView, CreatePurchaseView

urlpatterns = [
    path('purchases/', PurchasesView.as_view(), name='purchases_list'),
    path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchases/create/', CreatePurchaseView.as_view(), name='create_purchase'),
]