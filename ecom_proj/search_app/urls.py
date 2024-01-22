from django.urls import path
from . import views
app_name='search_app'
urlpatterns = [
    path('', views.s_result, name='s_result'),
]