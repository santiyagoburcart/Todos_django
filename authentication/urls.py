from django.urls import path
from .views import login_user, register, logout_user ,activate_user


urlpatterns = [
    path('login/', login_user, name = 'login'),
     path("logout_user/", logout_user, name='logout_user'),
    path('register/', register, name = 'register'),
    path('activate-user/<uidb64>/<token>/', activate_user, name = 'activate')


]
