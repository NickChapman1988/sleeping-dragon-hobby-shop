from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    """ Discount code model """
    code = models.CharField(max_length=10, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    amount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
