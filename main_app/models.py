from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from django.urls import reverse

# Create your models here.


class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    blooming_season = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('flowers_detail', kwargs={'pk': self.id})
    

class Butterfly(models.Model):

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    wingspan = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100)
    flowers = models.ManyToManyField(Flower)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        # self.id is referring to the cat that was just created
        # when the submit the form
        return reverse('detail', kwargs={'butterfly_id': self.id})

    def __str__(self):
        return f"{self.name} has {self.wingspan} mm long"
    
class Photo(models.Model):
	# url of the image on aws
    url = models.CharField(max_length=200)
    butterfly = models.ForeignKey(Butterfly, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for butterfly_id: {self.butterfly_id} @{self.url}" 
    
  
    

NECTAR_SOURCES = (
    ('B', 'Blossom'),
    ('T', 'Tree Sap'),
    ('Ft', 'Fruit'),
    ('Ot', 'Others'),
)

class NectarSource(models.Model):
    date = models.DateField('nectar source date')
    # source will be represented by a single letter (F)lowers, (T)ree Sap, (Ft)ruit, (Ot)hers
    source = models.CharField(max_length=2, choices=NECTAR_SOURCES, default=NECTAR_SOURCES[0][0])
    # Create a butterfly_id FK
    # models.CASCADE, if we delete a butterfly, delete its nectar sources as well
    butterfly = models.ForeignKey(Butterfly, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        # get_source_display is automatically generated,
        # on inputs that have choices parameter, see source
        return f"{self.get_source_display()} on {self.date}"
