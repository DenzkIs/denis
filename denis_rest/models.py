from django.db import models


class Profile(models.Model):
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname
