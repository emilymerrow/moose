from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
import uuid
import boto3

from .models import Butterfly, Flower, Photo
from botocore.exceptions import ClientError
from .forms import NectarSourceForm


BUCKET = 'emilymerrow'
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'


def add_photo(request, butterfly_id):
	# photo-file will be the "name" attribute on the <input name='photo-file' type='file'>
	photo_file = request.FILES.get('photo-file', None)
	if photo_file:
		# setup the aws client 
		s3 = boto3.client('s3')
		# Make a unique name to store the photo			# franklin.png
														# photo_file.name.rfind('.'): this gets us the file exstension .png
			 # store the file in a catcollector folder/randomnumber + the file name with the extension
		key = 'butterflycollection/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
		try:
			s3.upload_fileobj(photo_file, BUCKET, key)
			# build the url string of where it is hosted to store db
			url = f"{S3_BASE_URL}{BUCKET}/{key}"
			# add it to the db
			Photo.objects.create(url=url, butterfly_id=butterfly_id)
		except ClientError as e:
			print(e, " error from aws!")
		
	return redirect('detail', butterfly_id=butterfly_id)

def add_nectar_source(request, butterfly_id):
    form = NectarSourceForm(request.POST)
    if form.is_valid():
        new_nectar_source = form.save(commit=False)
        new_nectar_source.butterfly_id = butterfly_id
        new_nectar_source.save()
    return redirect('detail', butterfly_id=butterfly_id)


def assoc_flower(request, butterfly_id, flower_id):
    # associating a cat with a toy
    Butterfly.objects.get(id=butterfly_id).flowers.add(flower_id)

    # One line version of below ^
    # cat = Cat.object.get(id=cat_id)
    # cat.toys.add(toy_id)

    return redirect('detail', butterfly_id=butterfly_id)


class ButterflyCreate(CreateView):
    model = Butterfly
    fields = ['name', 'color', 'species', 'description', 'wingspan']
    def form_valid(self, form):
        # assing the logged in user (self.request.user)
        # to the the form instance that is being submitted when we 
        # send a post request ot the server
        form.instance.user = self.request.user
        # Let the createview do the rest of its job
        return super().form_valid(form)


class ButterflyUpdate(UpdateView):
    model = Butterfly
    # Disallow the name as input on the form, so no one can update the name
    fields = ['species', 'color', 'description', 'wingspan']


class ButterflyDelete(DeleteView):
    model = Butterfly
    success_url = '/butterflies/'


def butterfly_index(request):
    butterflies = Butterfly.objects.all()
    return render(request, 'butterflies/index.html', {'butterflies': butterflies})


def butterfly_detail(request, butterfly_id):
    butterfly = Butterfly.objects.get(id=butterfly_id)
    flowers_butterfly_doesnt_have = Flower.objects.exclude(
        id__in=butterfly.flowers.all().values_list('id'))
    nectar_source_form = NectarSourceForm()
    return render(request, 'butterflies/detail.html', {
        'butterfly': butterfly,
        'nectar_source_form': nectar_source_form,
        'flowers': flowers_butterfly_doesnt_have
    })


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class FlowerList(ListView):
    model = Flower


class FlowerCreate(CreateView):
    model = Flower
    fields = '__all__'


class FlowerDetail(DetailView):
    model = Flower


class FlowerUpdate(UpdateView):
    model = Flower
    fields = '__all__'


class FlowerDelete(DeleteView):
    model = Flower
    success_url = '/flowers/'

# def add_flower(request, butterfly_id):
#     butterfly = Butterfly.objects.get(id=butterfly_id)
#     form = FlowerForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         new_flower = form.save(commit=False)
#         new_flower.butterfly = butterfly
#         new_flower.save()
#         return redirect('butterfly_detail', butterfly_id=butterfly.id)
#     return render(request, 'butterflies/flower_form.html', {'form': form, 'butterfly': butterfly})
