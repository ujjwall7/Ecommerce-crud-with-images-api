from django.db import models


class Ecommerce(models.Model):
    Name=models.CharField(max_length=50)
    Price = models.IntegerField()
    Description = models.TextField()
    Image = models.FileField(upload_to="media")