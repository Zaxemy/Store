from django.urls import path
from products import views
from products.views import products


app_name = 'products'


urlpatterns = [
    path('', views.products, name='index')
]