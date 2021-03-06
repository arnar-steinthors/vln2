from django.contrib.auth.models import AbstractUser
from django.db import models
from shop.models import Product
from django_countries.fields import CountryField

# Create your models here.

DEFAULT_IMAGE = "https://www.kindpng.com/picc/m/495-4952535_create-digital-profile-icon-blue-user-profile-icon.png"


class Address(models.Model):
    full_name = models.CharField(max_length=70, blank=True, default="")
    address = models.CharField(max_length=32, blank=True, default="")
    country = CountryField(blank_label='(Select country)', multiple=False)
    city = models.CharField(max_length=32, blank=True, default="")
    postal_code = models.CharField(max_length=12, blank=True, default="")
    note = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.address


class User(AbstractUser):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=999)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32, default="", null=True)
    last_name = models.CharField(max_length=32, default="", null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=999, default=DEFAULT_IMAGE)
    enabled = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def validate_username(self):
        if len(self.username) > 12:
            return False
        usn = ''.join([i for i in self.username if not i.isdigit()])
        if not usn.isalpha():
            return False
        return True

    def get_address(self):
        return {
            'addr': self.address.address,
            'country': self.address.country,
            'city': self.address.city,
            'postal_code': self.address.postal_code,
            'note': self.address.note
        }

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product',)
