from celery import shared_task
from .models import User, Purchase

@shared_task
def print_text():
    print("Celery tasks - any text")

@shared_task
def print_purchases_count(user_id):
    try:
        user = User.objects.get(pk=user_id)
        purchases_count = Purchase.objects.filter(user=user).count()
        print(f"User ID: {user_id}, Purchases Count: {purchases_count}")
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist.")