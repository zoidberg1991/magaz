from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            OrderCreated.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
        if not form.is_valid():
            form_errors = form.errors
            return render(request, 'orders/order/create.html',
                          {'cart': cart, 'form': form, 'form_errors': form_errors})
    form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})