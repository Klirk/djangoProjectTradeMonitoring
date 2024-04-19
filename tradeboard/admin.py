from django.contrib import admin

from tradeboard.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']
