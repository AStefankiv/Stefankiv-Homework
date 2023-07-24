from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def users_view(request):
    users = User.objects.all()
    data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return JsonResponse(data, safe=False)