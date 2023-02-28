from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator

import random
from apps.cart.cart import Cart
from .forms import AddToCartForm

from .models import Category, Subcategory, Product
# Create your views here.


def category(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    query = category.products.all()
    paginator = Paginator(query, 6) # Show 6 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'product/category.html', {'products':products, })


def subcategory(request, category_slug, subcategory_slug):
    subcategory = get_object_or_404(Subcategory, category__slug=category_slug, slug=subcategory_slug)

    query = subcategory.products.all()
    paginator = Paginator(query, 6) # Show 6 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)


    return render(request, 'product/subcategory.html', {'products':products, })


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    # Cart Functionality
    cart = Cart(request)
    # Add to cart Section
    if request.method == "POST":
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    # Similar Products Section
    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >=4:
        similar_products = random.sample(similar_products, 4)

    context = { 'product':product,
                'similar_products':similar_products,
               }

    return render(request, 'product/product.html', context )

def search(request):
    query = request.GET.get('query', '')
    search_name=query
    products = Product.objects.filter(Q(name__icontains=query))

    paginator = Paginator(products, 9) # Show 6 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = { 'products':products,
                'query':query,
                'search_name':search_name,
               }

    return render(request, 'product/search.html',context )
