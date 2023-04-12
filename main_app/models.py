from django.db import models

# Create your models here.
from django.urls import reverse

# Create your models here.
class Butterfly(models.Model):

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    wingspan = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        # self.id is referring to the cat that was just created
        # when the submit the form
        return reverse('detail', kwargs={'butterfly_id': self.id})