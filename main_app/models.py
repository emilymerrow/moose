from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Butterfly(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=50, default='unknown')
    stage = models.CharField(max_length=50, default='unknown')

    def __str__(self):
        return self.name