from django.shortcuts import render
from products.models import Products, Category


def index(request):
    context = {
        'title': 'Shop - Главная страница'
        
    }
    
    
    return render(request, 'products/index.html', context)

def products(request):

    context = {
        'title': 'Store - Каталог',
        'products': Products.objects.all(),
        'categories': Category.objects.all(),        
    }
    return render(request, 'products/products.html', context)

