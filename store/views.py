from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Product, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tags.services import createTag

# Create your views here.

# products views ===============================================================
# product cuid functions

def index(request):
    # return HttpResponse("Hello, welcome to the store!")
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/index.html", context)


def show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/show.html", {"product": product})


@login_required
def create(request):
    return render(request, "products/create.html")


@login_required
def store(request):
    if request.method == "POST":
        name = request.POST.get("name")
        details = request.POST.get("details")
        qty = request.POST.get("qty")
        price = request.POST.get("price")

        product = Product(user=request.user, name=name, details=details, qty=qty, price=price)
        product.save()
        
        # Create a tag for the product
        tag = createTag(request)
        print("Created tag:", tag)

        return redirect("store.index")
    else:
        return redirect("store.index")


@login_required
def edit(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user != request.user:
        return messages.error(request, "You are not allowed to edit this product.")
    return render(request, "products/edit.html", {"product": product})


@login_required
def update(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        if product.user != request.user:
            return messages.error(request, "You are not allowed to edit this product.")

        product.name = request.POST.get("name")
        product.details = request.POST.get("details")
        product.qty = request.POST.get("qty")
        product.price = request.POST.get("price")
        product.save()
        return redirect("store.index")
    else:
        return redirect("store.index")


@login_required
def delete(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        if product.user != request.user:
            return messages.error(request, "You are not allowed to edit this product.")
        product.delete()
        return redirect("store.index")
    return redirect("store.index")


# cart views ===============================================================
# cart cuid functions


@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user).exclude(orderitem__isnull=False)
    for cart in carts:
        cart.total = cart.qty * cart.product.price
        # cart.selected = OrderItem.objects.filter(cart=cart).exists()
    context = {"carts": carts}
    return render(request, "cart/index.html", context)


@login_required
def cart_create(request):
    if request.method == "POST":
        user = request.user
        p = request.POST.get("product")
        product = get_object_or_404(Product, id=p)
        qty = request.POST.get("qty")
        if int(qty) > product.qty:
            return HttpResponse("Not enough stock available.")
        cart = Cart(user=user, product=product, qty=qty)
        product.qty -= int(qty)
        cart.save()
        product.save()
        return redirect("cart.index")
    else:
        return redirect("cart.index")


@login_required
def cart_delete(request, id):
    if request.method == "POST":
        cart = get_object_or_404(Cart, id=id)
        if cart.user != request.user:
            return messages.error(
                request, "You are not allowed to delete this cart item."
            )
        cart.delete()
        return redirect("cart.index")
    return redirect("cart.index")


# order views ===============================================================
# order create function


@login_required
def order_index(request):
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "order/index.html", context)


@login_required
def order_show(request, id):
    order = get_object_or_404(Order, id=id)
    order.id_text = str(order.id).zfill(6)
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        item.cart.total = item.cart.qty * item.cart.product.price
    context = {"order": order, "order_items": order_items}
    return render(request, "order/show.html", context)


@login_required
def order_create(request):
    if request.method == "POST":
        carts = Cart.objects.filter(id__in=request.POST.getlist("selected"))
        if not carts:
            return HttpResponse("Your cart is empty.")
        order = Order(user=request.user)
        order.total_price = sum(cart.qty * cart.product.price for cart in carts)
        order.save()
        last_order = Order.objects.filter(user=request.user).latest("created_at")
        for cart in carts:
            order_item = OrderItem(order=last_order, cart=cart)
            order_item.save()
        return redirect("cart.index")
    else:
        return redirect("cart.index")
