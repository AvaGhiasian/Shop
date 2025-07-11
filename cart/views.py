from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart
from django.http import JsonResponse
from .common.KaveSms import send_sms_normal, send_sms_with_template


# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    try:
        quantity = request.POST['quantity']
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)

        for _ in range(int(quantity)):
            cart.add(product)

        cart_quantity = cart.cart[str(product_id)]['quantity']

        if product.inventory == cart_quantity:
            count = True
        else:
            count = False
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'cart_count': count,
        }
        send_sms_normal('09912975826','محصول به سبد خرید اضافه شد')
        return JsonResponse(context)
    except:
        return JsonResponse({"error": "Invalid request."})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST
def update_quantity(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        if action == 'add':
            cart.add(product)
        elif action == 'decrease':
            cart.decrease(product)

        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'quantity': cart.cart[item_id]['quantity'],
            # 'price': cart.cart[item_id]['price'],
            'total': cart.cart[item_id]['quantity'] * cart.cart[item_id]['price'],
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'Item not found!'})


@require_POST
def remove_item(request):
    item_id = request.POST.get('item_id')
    print(item_id)
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart.remove(product)

        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'Item not found!'})
