from django.urls import path
from . import views as view
urlpatterns = [
    path('login/', view.login, name='login'),      
    path('register/', view.register, name='register'),

    path('logout/', view.logout, name='logout'),
]