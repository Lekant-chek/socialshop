from django.shortcuts import render


def index(request):
    context = {'title': 'SocialShop'}
    return render(request, 'productsapp/index.html', context)


def products(request):
    context = {'title': 'SocialShop - Каталог'}
    return render(request, 'productsapp/products.html', context)
