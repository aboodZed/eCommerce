from django.urls import path
from . import views as view
urlpatterns = [
    path('', view.index, name='store.index'),
    path('show/<int:id>/', view.show, name='product.show'),
    path('create/', view.create, name='product.create'),
    path('store/', view.store, name='product.store'),
    path('edit/<int:id>/', view.edit, name='product.edit'),
    path('update/<int:id>/', view.update, name='product.update'),
    path('delete/<int:id>/', view.delete, name='product.delete'),
    
    path('cart/', view.cart, name='cart.index'),
    path('cart/create/', view.cart_create, name='cart.create'),
    path('cart/delete/<int:id>/', view.cart_delete, name='cart.delete'),
    
    path('order/', view.order_index, name='order.index'),
    path('order/show/<int:id>/', view.order_show, name='order.show'),
    path('order.create/', view.order_create, name='order.create'),
]