from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Pompe

class PompeListView(ListView):
    model = Pompe
    template_name = 'pompe_list.html'
    context_object_name = 'pompes'

class PompeCreateView(CreateView):
    model = Pompe
    template_name = 'pompe/pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']

    def get_success_url(self):
        return reverse_lazy('pompe:pompe_list')





class PompeUpdateView(UpdateView):
    model = Pompe
    template_name = 'pompe/pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']
    def get_success_url(self):
      return reverse_lazy('pompe:pompe_list')


class PompeDeleteView(DeleteView):
    model = Pompe
    template_name = 'pompe/pompe_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('pompe:pompe_list')

