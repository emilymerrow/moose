from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
 # Note that parens are optional if not inheriting from another class

class Butterfly:
    def __init__(self, name, color, description, stage):
        self.name = name
        self.color = color
        self.description = description
        self.stage = stage

butterflies = [
    Butterfly('Monarch', 'orange and black', 'migrates south for the winter', 'adult'),
    Butterfly('Swallowtail', 'yellow and black', 'has long tails on its wings', 'pupa'),
    Butterfly('Blue Morpho', 'bright blue', 'found in rainforests', 'larva')
]




# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')

def butterfly_index(request):
  return render(request, 'butterflies/index.html', { 'butterflies': butterflies })