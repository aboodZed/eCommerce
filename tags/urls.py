from django.urls import path
from . import views as view

urlpatterns = [
    path('', view.index, name='tag.index'),
    path('store/', view.store, name='tag.store'),
]