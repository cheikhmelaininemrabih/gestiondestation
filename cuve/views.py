from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cuve

def index(request):
    return render(request, 'cuve/index.html')

class CuveListView(ListView):
    model = Cuve
    template_name = 'cuve_list.html'
    context_object_name = 'cuve'

class CuveCreateView(CreateView):
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    
    def get_success_url(self):
        return reverse('cuve_list')

class CuveUpdateView(UpdateView):
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    
    def get_success_url(self):
        return reverse('cuve_list')

class CuveDeleteView(DeleteView):
    model = Cuve
    template_name = 'cuve/cuve_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('cuve_list')
