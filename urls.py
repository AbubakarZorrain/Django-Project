from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import re_path
urlpatterns = [

path('about/',views.about, name="about"),
path('outdoor/',views.outdoor, name="outdoor"),
path('indoor/',views.indoor, name="indoor"),
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
path('signup/', views.signup, name='signup'),
re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
path('customer/',views.customers, name="customer"),
path('dashboard/',views.dashboard, name="dashboard"),
path('main',views.main,name="main"),
path('mainb',views.mainb,name="mainb"),
path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('email',views.email, name='email'),

path('cart_add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
    path('new_arrival/', views.new_arrival, name='new_arrival'),
    path('customer_info/',views.customer_info, name="customer_info"),
    path('comments/',views.comments, name="comments"),
    ]