from django.shortcuts import render, redirect
from django.views import View
from .models import Purchase
from .forms import PurchaseForm

class PurchasesView(View):
    def get(self, request):
        purchases = Purchase.objects.all()
        return render(request, 'purchases_list.html', {'purchases': purchases})

class PurchaseDetailView(View):
    def get(self, request, id):
        purchase = Purchase.objects.get(pk=id)
        return render(request, 'purchase_detail.html', {'purchase': purchase})

class CreatePurchaseView(View):
    def get(self, request):
        form = PurchaseForm()
        return render(request, 'create_purchase.html', {'form': form})

    def post(self, request):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchases_list')
        return render(request, 'create_purchase.html', {'form': form})