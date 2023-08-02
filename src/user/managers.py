from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, is_superuser, is_staff, is_active,
                     password=None):
        user = self.model(
            username=username,
            is_superuser=is_superuser,
            is_active=is_active,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None):
        return self._create_user(
            username=username,
            is_superuser=False,
            is_staff=True,
            is_active=True,
            password=password,
        )

    def create_superuser(self, username, password=None):
        return self._create_user(
            username=username,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            password=password,
        )
