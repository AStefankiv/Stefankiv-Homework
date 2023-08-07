from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import UserForm
from rest_framework import viewsets, pagination
from .serializers import UserSerializer
from .filters import UserFilter
from .tasks import print_text, print_purchases_count
from celery import shared_task
from .models import User, Purchase

class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, id):
        try:
            user = User.objects.get(pk=id)
            print_purchases_count.delay(id)
            return render(request, 'user_detail.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'user_not_found.html')

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']

            print_text.delay(f"New user created: {username}")

            return redirect('users_list')
        return render(request, 'create_user.html', {'form': form})


class UserPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filterset_class = UserFilter


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls