from django.db import models


class Profile(models.Model):
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title
