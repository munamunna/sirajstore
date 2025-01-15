from django.db import models



from django.db import models
from accounts.models import *

# Category for products/services
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Product or Service
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name


# Cart for User
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.username}"


# Cart Items
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# Country for selection
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name




class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel_images/")
    caption = models.CharField(max_length=255, blank=True, null=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carousel Image {self.id}"
