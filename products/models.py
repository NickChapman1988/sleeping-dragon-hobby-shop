from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, blank=True)
    description = models.TextField()
    stock = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=1)
    width = models.DecimalField(max_digits=6, decimal_places=1)
    height = models.DecimalField(max_digits=6, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_rating(self):
        """ Calculate product rating from reviews """
        self.rating = self.reviews.all().aggregate(Avg(
            'rating'))['rating__avg']
        self.save()
        return self.rating


class Review(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True,
        related_name='reviews', on_delete=models.SET_NULL)
    content = models.TextField(null=False, blank=False)
    rating = models.IntegerField(
        null=False, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ", " + str(self.product)
