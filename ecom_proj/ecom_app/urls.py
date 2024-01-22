from django.urls import path
from . import views
app_name='ecom_app'
urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:catslug>/', views.allprodcat, name='catwiseprods'),
    path('<slug:catslug>/<slug:product_slug>/', views.productdetails, name='prod_det_pathname'),
]