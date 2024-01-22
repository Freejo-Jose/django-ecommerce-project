from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartItem
from .views import cartid


def counter(request):
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cartid(request))
            cartitems=CartItem.objects.all().filter(cart=cart[:1])
            for ci in cartitems:
                cart_count+=ci.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
