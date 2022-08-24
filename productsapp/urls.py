from django.urls import path
from productsapp.views import products

app_name = 'product'

urlpatterns = [
    path('', products, name='index'),
    path('<int:id>/', products, name='product'),
]