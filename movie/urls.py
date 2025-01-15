from django.urls import path
from .views import CategoryListView, ProductListView, CartDetailView, CountryListView,ProductByCategoryView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('countries/', CountryListView.as_view(), name='country-list'),
     path('products/category/<int:category_id>/', ProductByCategoryView.as_view(), name='products-by-category'),
]
