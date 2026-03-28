from django.contrib import admin
from django.urls import path, include
from project import views 

urlpatterns = [ 
   path('home', views.home, name='home'),
   path('dashboard', views.dashboard, name='dashboard'), 
   path('header', views.header, name='header'),
   path('sidebar', views.sidebar, name='sidebar'),

   # Category
   path('category', views.category, name='category'),
   path('category_table', views.category_table, name='category_table'),
   path('category_store', views.category_store, name='category_store'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('category_edite/<int:id>', views.category_edite, name='category_edite'),
   path('category_update/<int:id>', views.category_update, name='category_update'),

   # Subcategory
   path('subcategory', views.subcategory, name='subcategory'),
   path('subcategory_table', views.subcategory_table, name='subcategory_table'),
   path('subcategory_store', views.subcategory_store, name='subcategory_store'),
   path('delete_sub/<int:id>', views.delete_sub, name='delete_sub'),
   path('subcategory_edit/<int:id>', views.subcategory_edit, name='subcategory_edit'),
   path('subcategory_update/<int:id>', views.subcategory_update, name='subcategory_update'),

   # Subcategory
   path('product', views.product, name='product'),
   path('product_table', views.product_table, name='product_table'),
   path('product_store', views.product_store, name='product_store'),
   path('product_details/<int:id>', views.product_details, name='product_details'),
   path('product_delete/<int:id>', views.product_delete, name='product_delete'),
   path('product_edit/<int:id>', views.product_edit, name='product_edit'),
   path('product_update/<int:id>', views.product_update, name='product_update'),

   # State
   path('state', views.state, name='state'),
   path('state_table', views.state_table, name='state_table'),
   path('state_store', views.state_store, name='state_store'),
   path('state_delete/<int:id>', views.state_delete, name='state_delete'),
   path('state_edite/<int:id>', views.state_edite, name='state_edite'),
   path('state_update/<int:id>', views.state_update, name='state_update'),


   # City
   path('city', views.city, name='city'),
   path('city_table', views.city_table, name='city_table'),
   path('city_store', views.city_store, name='city_store'),
   path('city_delete/<int:id>', views.city_delete, name='city_delete'),
   path('city_edite/<int:id>', views.city_edite, name='city_edite'),
   path('city_update/<int:id>', views.city_update, name='city_update'),

   # Area
   path('area', views.area, name='area'),
   path('area_table', views.area_table, name='area_table'),
   path('area_store', views.area_store, name='area_store'),
   path('area_delete/<int:id>', views.area_delete, name='area_delete'),
   path('area_edit/<int:id>', views.area_edit, name='area_edit'),
   path('area_update/<int:id>', views.area_update, name='area_update'),

   path('inquiry_list', views.inquiry_list, name='inquiry_list'),
   path('register_table', views.register_table, name='register_table'),
   path('feedback', views.feedback, name='feedback'),
   path('user', views.user, name='user'),
]
