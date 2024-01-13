from .models import User
from .serializers import UserSerializer
from random import choice
class UserService:

    @staticmethod
    def get_users():
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def get_users_and_followers():
        users = User.objects.all()
        response = []

        for user in users:
            response.append(
                {
                    'user_id': user.user_id,
                    'followers': [follower.user_id for follower in users
                                    if user.user_id in follower.users_following]
                }
            )
        return response
    
    @staticmethod
    def get_least_followers_user():
        users = User.objects.all()

        min_followers = users.count()
        followers_map = dict()

        for user in users:
            temp_user = {
                'user_id': user.user_id,
                'amount_of_followers': len([follower.user_id for follower in users
                                if user.user_id in follower.users_following])
                }

            follower_count = temp_user['amount_of_followers']
            followers_map[follower_count] = followers_map.get(follower_count, []) + [temp_user]
            min_followers = min(min_followers, follower_count)

        return choice(followers_map[min_followers])