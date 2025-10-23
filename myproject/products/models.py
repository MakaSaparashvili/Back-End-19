from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
