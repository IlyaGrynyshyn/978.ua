from django.shortcuts import render
from cart.cart import Cart
from mainapp.models import Category
from .models import OrderItem,Order
from .forms import OrderCreateForm
from mainapp.models import Product


def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            Order.customer = request.user
            user = Order.customer
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
                product = Product.objects.filter(title__icontains=item['product']).update(ordered=+int(1))
                
            cart.clear()
            return render(request, 'order/created.html', {'order': order, 'categories':categories})
    else:
        form = OrderCreateForm()
    return render(request, 'order/telemart.html', {'cart': cart, 'form': form, 'categories':categories})
