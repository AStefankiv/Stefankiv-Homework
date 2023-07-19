from django.urls import path
from . import views

urlpatterns = [
    path('purchases/', views.purchase_list_json, name='purchase_list_json'),
]
