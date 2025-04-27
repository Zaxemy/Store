from django.contrib import admin
from users.models import User
# Register your models here.

from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [BasketAdmin]