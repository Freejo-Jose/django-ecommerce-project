from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listview/', views.listview.as_view(), name='listview'),
    path('detailview/<int:pk>/', views.detailview.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.updateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.deleteview.as_view(), name='deleteview'),
]
