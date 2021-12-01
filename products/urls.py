from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_management/', views.product_management, name='product_management'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('product_management/edit_category/<category_id>/', views.edit_category, name='edit_category'),
]
