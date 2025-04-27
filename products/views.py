from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, Category, Basket
from users.models import User
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'Shop - Главная страница'
        
    }
    
    
    return render(request, 'products/index.html', context)










def products(request, category_id=None, page_number=1):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    
        
        
        
    context = {
        'title': 'Store - Каталог',
        'products': products_paginator,
        'categories': Category.objects.all(),        
    }
    return render(request, 'products/products.html', context)















def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user,product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

