from django.contrib import admin

# Register your models here.
from .models import Butterfly, NectarSource, Flower

# Add our Butterfly, NectarSource, and Flower models to the admin site,
# so we can perform CRUD operations on them!
admin.site.register(Butterfly)
admin.site.register(NectarSource)
admin.site.register(Flower)
