from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models

# Create your models here.
class Butterfly(models.Model):

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    wingspan = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'butterfly_id : self.id'})