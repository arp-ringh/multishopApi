import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from apps.order.models import OrderItem

from .cart import Cart
from .forms import CheckoutForm
from apps.order.utilities import checkout, notify_vendor, notify_customer

from apps.customers.decorators import customer_required
from django.contrib.auth.decorators import login_required

def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity')

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart:cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart:cart')

    return render(request, 'cart/cart.html', {})



@login_required
@customer_required
def cart_checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']
            try:
                charge = stripe.Charge.create(
                    amount=int(cart.get_total_cost() * 100),
                    currency='USD',
                    description='Charge from MultiShop',
                    source=stripe_token
                )

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = checkout(request, first_name, last_name, email, address, zipcode, place, phone, cart.get_total_cost())

                cart.clear()

                #notify_customer(order)
                #notify_vendor(order)

                return redirect('cart:success')

            except Exception:
                messages.error(request, "There was something wrong with the payment")
    else:
        form = CheckoutForm()

    return render(request, 'cart/cartcheckout.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY})


@login_required
@customer_required
def checkout_success(request):
    current_user = request.user
    orderitems = OrderItem.objects.all()



    return render(request, 'cart/success.html', {'orderitems':orderitems, 'current_user':current_user})
