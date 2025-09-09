from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Plant, CareLog

def home(request):
    return render(request, 'home.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)
    care_logs = plant.care_logs.all()[:5]  # Get the 5 most recent care logs
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'care_logs': care_logs
    })

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'plant_type', 'watering_frequency', 'notes', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name', 'plant_type', 'watering_frequency', 'notes', 'image']
    
    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'
    
    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

# Care Log Views
class CareLogCreate(LoginRequiredMixin, CreateView):
    model = CareLog
    fields = ['activity', 'date', 'notes']
    template_name = 'main_app/carelog_form.html'
    
    def form_valid(self, form):
        # Get the plant and ensure it belongs to the current user
        plant = get_object_or_404(Plant, id=self.kwargs['plant_id'], user=self.request.user)
        form.instance.plant = plant
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant'] = get_object_or_404(Plant, id=self.kwargs['plant_id'], user=self.request.user)
        return context

class CareLogUpdate(LoginRequiredMixin, UpdateView):
    model = CareLog
    fields = ['activity', 'date', 'notes']
    template_name = 'main_app/carelog_form.html'
    
    def get_queryset(self):
        return CareLog.objects.filter(plant__user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant'] = self.object.plant
        return context

class CareLogDelete(LoginRequiredMixin, DeleteView):
    model = CareLog
    template_name = 'main_app/carelog_confirm_delete.html'
    
    def get_queryset(self):
        return CareLog.objects.filter(plant__user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('plant_detail', kwargs={'plant_id': self.object.plant.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant'] = self.object.plant
        return context

@login_required
def care_logs_index(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)
    care_logs = plant.care_logs.all()
    return render(request, 'care_logs/index.html', {
        'plant': plant,
        'care_logs': care_logs
    })

# Authentication Views
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plants_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def all_care_logs(request):
    # Get all care logs for all plants belonging to the user
    care_logs = CareLog.objects.filter(plant__user=request.user)
    return render(request, 'care_logs/all_care_logs.html', {
        'care_logs': care_logs
    })

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')