from django.forms import ModelForm
from .models import NectarSource, Flower

class NectarSourceForm(ModelForm):
    class Meta:
        model = NectarSource
        fields = ['date', 'source']

class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'