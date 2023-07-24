from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchases_view, name='purchases_hw'),
]