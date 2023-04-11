from django.shortcuts import render
from django.views.generic.edit import CreateView

# Add the following import
from django.http import HttpResponse

from .models import Butterfly
class ButterflyCreate(CreateView):
  model = Butterfly
  fields = '__all__'
  success_url = '/butterflies/'
  
# Add the Cat class & list and view function below the imports
 # Note that parens are optional if not inheriting from another class

def butterfly_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  return render(request, 'butterflies/detail.html', {'butterfly': butterfly})

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')

def butterfly_index(request):
  butterflies = Butterfly.objects.all()
  return render(request, 'butterflies/index.html', { 'butterflies': butterflies })
