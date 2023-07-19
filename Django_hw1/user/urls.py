from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list_json, name='user_list_json'),
]