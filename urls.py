from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

path('about/',views.about, name="about"),
path('blog/',views.blog, name="blog"),
path('blog-details/',views.blog_detail, name="blog-details"),
path('cart/',views.cart, name="cart"),
path('checkout/',views.checkout, name="checkout"),
path('confirmation/',views.confirmation, name="confirmation"),
path('contact/',views.contact, name="contact"),
path('elements/',views.element, name="elements"),
path('',views.index, name="index"),
path('index',views.index, name="index"),
path('login/',views.loginpage, name='login'),
path('logout/',views.logoutUser, name='logout'),
path('product_details/<slug:slug>/',views.product_details, name="product-details"),
path('shop/',views.shop, name="shop"),
path('signup/',views.register, name="signup"),
path('customer/',views.customers, name="customer"),
path('dashboard/',views.dashboard, name="dashboard"),
path('main',views.main,name="main"),
path('mainb',views.mainb,name="mainb"),

]