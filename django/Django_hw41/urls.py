"""
URL configuration for Django36 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import router as router
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books_hw.views import BookViewSet
from purchases_hw.views import PurchaseViewSet
from users_hw.views import UserViewSet

import tasks

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls')),
    path('users_hw/', include('users_hw.urls')),
    path('books_hw/', include('books_hw.urls')),
    path('purchases_hw/', include('purchases_hw.urls')),
    path('api/', include('books_hw.urls')),
    path('api/', include('purchases_hw.urls')),
    path('api/', include('users_hw.urls')),
]

urlpatterns += router.urls

