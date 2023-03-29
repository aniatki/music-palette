from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('<artwork_id>', views.product_view, name='product'),
]
