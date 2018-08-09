from django.db import models
from datetime import datetime

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Products"