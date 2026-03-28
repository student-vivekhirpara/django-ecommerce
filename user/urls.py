from django.contrib import admin
from django.urls import path, include
from user import views 

urlpatterns = [
	path('base', views.base, name='base'),
	path('home', views.home, name='home'),
	path('header', views.header, name='header'),
	path('footer', views.footer, name='footer'),

	path('inquiry', views.inquiry, name='inquiry'),
	path('inquiry_store', views.inquiry_store, name='inquiry_store'),

	path('register', views.register, name='register'),
	path('register_store', views.register_store, name='register_store'),

	path('login', views.login, name='login'),
	path('login_verify', views.login_verify, name='login_verify'),
	path('logout', views.logout, name='logout'),

	path('profile', views.profile, name='profile'),

	path('feedback', views.feedback, name='feedback'),
	path('feedback_store', views.feedback_store, name='feedback_store'),

	path('user_profile', views.user_profile, name='user_profile'),
	path('edit_profile', views.edit_profile, name='edit_profile'),
	path('update_profile', views.update_profile, name='update_profile'),

	path('change_password', views.change_password, name='change_password'),
	path('change_password_check', views.change_password_check, name='change_password_check'),
	path('forgate_password', views.forgate_password, name='forgate_password'),
	path('forgate_password_check', views.forgate_password_check, name='forgate_password_check'),



	path('product', views.product, name='product'),
	path('shop_detail/<int:id>/', views.shop_detail, name='shop_detail'),

	path('cart', views.cart, name='cart'),
	path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
	path('cart_delete/<int:id>/', views.cart_delete, name='cart_delete'),
	path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
	
	
	path('product_checkout', views.product_checkout, name='product_checkout'),
	path('place_order', views.place_order, name='place_order'),

	path('payment_process', views.payment_process, name='payment_process'),
    path('success', views.success, name='success'),
    path('order', views.order, name='order'),
]