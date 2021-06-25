from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email','is_staff', 'is_email_verified')
    search_fields = ('username', 'email',)
    list_per_page = 30




admin.site.register(User, UserAdmin)
