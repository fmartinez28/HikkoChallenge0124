from .views import get_users_followers, get_least_followers_user
from django.urls import path

urlpatterns = [
    path('', get_users_followers, name='usersandfollowers'),
    path('leastfollowers/', get_least_followers_user, name='leastfollowers'),
]