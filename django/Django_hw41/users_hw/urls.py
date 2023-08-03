from django.urls import path
from .views import UsersView, UserDetailView, CreateUserView

urlpatterns = [
    path('users/', UsersView.as_view(), name='users_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
]