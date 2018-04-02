from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Product

def main(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'main.html', context)

def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'products/index.html', context)

def cart(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'cart/cart.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

def addToCart(request, product_id):
    response = "You're sending %s to your cart products."
    return HttpResponse(response % product_id)

def addToFavorites(request, product_id):
    return HttpResponse("You're adding %s to your favorites product." % product_id)
