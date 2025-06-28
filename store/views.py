from django.shortcuts import render, get_object_or_404

from .models import Category, Product


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, "store/list.html", context)


def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id)

    context = {
        'product': product,
    }
    return render(request, "store/detail.html", context)
