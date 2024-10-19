from django.urls import path
from .views import register, home, custom_user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('login/', custom_user_login, name='custom_user_login'),
]
