from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name="user_logout"),
    

]