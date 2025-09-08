from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant

def home(request):
    return render(request, 'home.html')

def plants_index(request):
    plants = Plant.objects.all()  # Show all plants instead of user-specific
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'plant_type', 'watering_frequency', 'notes', 'image']
    
    # Remove the form_valid method that assigns user

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'plant_type', 'watering_frequency', 'notes', 'image']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'