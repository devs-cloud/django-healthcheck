from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from hc.accounts.models import Profile


class BasicBackend(object):

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


# Authenticate against the token in user's profile.
class ProfileBackend(BasicBackend):

    def authenticate(self, request=None, username=None, token=None):
        try:
            profiles = Profile.objects.select_related("user")
            profile = profiles.get(user__username=username)
        except Profile.DoesNotExist:
            return None

        if not check_password(token, profile.token):
            return None

        return profile.user


class EmailBackend(BasicBackend):

    def authenticate(self, request=None, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
