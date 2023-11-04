from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Station
from django.urls import reverse_lazy

class StationListView(ListView):
    model = Station
    template_name = 'station_list.html'
    context_object_name = 'stations'

class StationCreateView(CreateView):
    model = Station
    template_name = 'station_form.html'
    fields = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes', 'id_users']
    def get_success_url(self):
        return reverse('station_list')

class StationUpdateView(UpdateView):
    model = Station
    template_name = 'station_form.html'
    fields = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes', 'id_users']
    def get_success_url(self):
        return reverse('station_list')

class StationDeleteView(DeleteView):
    model = Station
    template_name = 'station_confirm_delete.html'

    def get_success_url(self):
        return reverse('station_confirm_list')