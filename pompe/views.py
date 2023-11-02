from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Pompe

class PompeListView(ListView):
    model = Pompe
    template_name = 'pompe/pompe_list.html'
    context_object_name = 'pompe_list'

class PompeCreateView(CreateView):
    model = Pompe
    template_name = 'pompe/pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']
    success_url = '/pompe/'

class PompeDetailView(DetailView):
    model = Pompe
    template_name = 'pompe/pompe_detail.html'
    context_object_name = 'pompe'

class PompeUpdateView(UpdateView):
    model = Pompe
    template_name = 'pompe/pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']
    success_url = '/pompe/'

class PompeDeleteView(DeleteView):
    model = Pompe
    template_name = 'pompe/pompe_confirm_delete.html'
    success_url = '/pompe/'
