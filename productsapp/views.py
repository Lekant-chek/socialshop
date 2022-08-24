from django.shortcuts import render

from productsapp.models import ProductCategory, Product


def index(request):
    context = {'title': 'SocialShop'}
    return render(request, 'productsapp/index.html', context)


def products(request):
    context = {
        'title': 'SocialShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'productsapp/products.html', context)
