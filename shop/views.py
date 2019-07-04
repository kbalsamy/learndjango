from django.shortcuts import render, get_object_or_404
# from django.views.generic.list import ListView
from .models import Catagory, Product

# Create your views here.


def product_List(request, catagory_slug=None):

    catagory = None
    catagory = Catagory.objects.all()
    product = Product.objects.filter(available=True)
    if catagory_slug:
        catagory = get_object_or_404(Catagory, slug=catagory_slug)
        product = Product.objects.filter(catagory=catagory)

    return render(request, 'shop/product/list.html', {'catagory': catagory, 'product': product})


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'shop/product/detail.html', {'product': product})
