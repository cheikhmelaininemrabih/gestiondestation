from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pompiste

class PompisteListView(ListView):
    model = Pompiste
    template_name = 'pompiste/pompiste_list.html'
    context_object_name = 'pompistes'

class PompisteCreateView(CreateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']

    def get_success_url(self):
        return reverse_lazy('pompiste_list')

class PompisteUpdateView(UpdateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']

    def get_success_url(self):
        return reverse_lazy('pompiste_list')

class PompisteDeleteView(DeleteView):
    model = Pompiste
    template_name = 'pompiste/pompiste_confirm_delete.html'
    context_object_name = 'pompiste'

    def get_success_url(self):
        return reverse_lazy('pompiste_list')
