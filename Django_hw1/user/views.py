from django.http import JsonResponse
from .models import User

def user_list_json(request):
    users = User.objects.all()

    users_json = [{"username": user.username, "email": user.email} for user in users]

    return JsonResponse(users_json, safe=False)