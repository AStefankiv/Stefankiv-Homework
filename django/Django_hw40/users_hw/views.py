from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import UserForm

class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'user_detail.html', {'user': user})

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')
        return render(request, 'create_user.html', {'form': form})