from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year = models.CharField(max_length=4)  # Or models.DateField if you want to store full date

    def __str__(self):
        return f"{self.degree} - {self.institution} ({self.year})"


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

# class AddToCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user.username} - {self.product.title}"
# class Checkout(models.Model):
#     pass
# class OrderHistory(models.Model):
#    pass