from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Pompe

class PompeListView(ListView):
    model = Pompe
    template_name = 'pompe_list.html'
    context_object_name = 'pompe'

class PompeCreateView(CreateView):
    model = Pompe
    template_name = 'pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']

    def get_success_url(self):
        return reverse('pompe_list')


# views.py
class PompeDetailView(DetailView):
    model = Pompe
    template_name = 'pompe_detail.html'
    context_object_name = 'pompe'

# views.py
class PompeUpdateView(UpdateView):
    model = Pompe
    template_name = 'pompe_form.html'
    fields = ['type', 'model', 'id_cuve', 'id_pompiste']

    def get_success_url(self):
        return reverse('pompe_list')

# views.py
class PompeDeleteView(DeleteView):
    model = Pompe
    template_name = 'pompe_confirm_delete.html'

    def get_success_url(self):
        return reverse('pompe_list')
