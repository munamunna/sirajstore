from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework import generics
from .models import Category, Product, Cart, Country,CarouselImage
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CountrySerializer,CarouselImageSerializer


# Categories API
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Products API
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()


# Cart API
class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        return self.request.user.cart


# Countries API
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class CarouselImageViewSet(ModelViewSet):
    queryset = CarouselImage.objects.all().order_by('-created_at')
    serializer_class = CarouselImageSerializer


from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductByCategoryView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
