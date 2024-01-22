from django.urls import path
from . import views
app_name='cart_app'
urlpatterns = [
    path('<int:productid>/', views.add2cart, name='add2cart'),
    path('detail/', views.cartdetail, name='cartdetail'),
    path('remfromcart/<int:productid>', views.remfromcart, name='remfromcart'),
    path('minuscart/<int:productid>', views.minuscart, name='minuscart'),
]