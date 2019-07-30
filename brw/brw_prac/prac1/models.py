from django.db import models

class Product (models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField()
    price = models.IntegerField()

created_at = models.DateTimeField(auto_now_add=True)
update_at = models.DateTimeField(auto_now=True)

# Create your models here.
