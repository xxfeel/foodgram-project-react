from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name',)
    list_filter = ('username', 'email',)
    search_fields = ('username', 'email',)
    empty_value_display = 'не заполнено'
