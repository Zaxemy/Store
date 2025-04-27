from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, Category, Basket
from users.models import User

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

