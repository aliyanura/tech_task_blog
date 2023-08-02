from django.contrib import admin
from src.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_superuser', 'is_staff')
    list_display_links = ('username',)
    list_filter = ('username', 'is_active', 'is_superuser', 'is_staff')
