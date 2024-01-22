from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from ecom_app.models import Product
from cart_app.models import Cart,CartItem

# Create your views here.
def cartid(request):
    cid=request.session.session_key
    if not cid:
        cid=request.session.create()
    return cid

def add2cart(request,productid):
    product=Product.objects.get(id=productid)
    try:
        cart=Cart.objects.get(cart_id=cartid(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cartid(request))
        cart.save()
    try:
        cartitem=CartItem.objects.get(cart=cart,product=product)
        if cartitem.quantity < product.stock and product.available:
            cartitem.quantity+=1
            cartitem.save()
    except CartItem.DoesNotExist:
        if product.available and product.stock>0:
            cartitem=CartItem.objects.create(cart=cart,product=product,quantity=1)
            cartitem.save()
    return redirect('cart_app:cartdetail')
def cartdetail(request,cartvalue=0,cartcount=0,cartitems=None):
    try:
        cart=Cart.objects.get(cart_id=cartid(request))
        cartitems=CartItem.objects.filter(cart=cart,active=True)
        for ci in cartitems:
            cartvalue+=ci.subtotal()
            cartcount+=ci.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartvalue=cartvalue,cartcount=cartcount,cartitems=cartitems))

def minuscart(request,productid):
    cart = Cart.objects.get(cart_id=cartid(request))
    prod = get_object_or_404(Product, id=productid)
    cartitem=CartItem.objects.get(cart=cart,product=prod)
    if cartitem.quantity > 1:
        cartitem.quantity-=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart_app:cartdetail')
def remfromcart(request,productid):
    cart = Cart.objects.get(cart_id=cartid(request))
    prod = get_object_or_404(Product, id=productid)
    cartitem=CartItem.objects.get(cart=cart,product=prod)
    cartitem.delete()
    return redirect('cart_app:cartdetail')


