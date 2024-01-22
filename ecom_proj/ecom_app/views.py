from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def allprodcat(request,catslug=None):
    if catslug!=None:
        pagecat=get_object_or_404(Category, slug=catslug)
        products_list=Product.objects.all().filter(category=pagecat,available=True)
    else:
        pagecat = None
        products_list = Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':pagecat,'products':products})

def productdetails(request,catslug,product_slug):
    try:
        product=Product.objects.get(category__slug=catslug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
