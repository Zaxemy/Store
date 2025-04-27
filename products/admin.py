from django.contrib import admin
from products.models import Category, Products, Basket

#Register your models here


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', 'price', 'quantity', 'image', 'category']
    search_fields = ['name', 'description']
    ordering = ['name']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fields = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']
    

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity']