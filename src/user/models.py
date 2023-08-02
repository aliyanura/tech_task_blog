from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from src.common.models import BaseModel
from src.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=15, blank=False,
                                null=False, unique=True,
                                verbose_name=("Имя пользователя"))
    password = models.CharField(max_length=128, blank=True,
                                null=True, verbose_name=("Пароль"))
    is_active = models.BooleanField(default=True,
                                    verbose_name=("Является активным"))
    is_staff = models.BooleanField(
        default=False, verbose_name=("Является сотрудником системы")
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name=("Является администратором системы")
    )

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("username",)