from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Station
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required



def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)  
    return render(request, 'stations/station_detail.html', {'station': station})

def station_list(request):
    station = Station.objects.all() 
    return render(request, 'stations/station_list.html', {'station': station})

class StationListView(ListView):
    model = Station
    template_name = 'station/station_list.html'
    context_object_name = 'stations'


class StationCreateView(CreateView):
    model = Station
    template_name = 'station/station_form.html'
    fields = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes', 'id_users']
    success_url = reverse_lazy('station:station_list')

class StationUpdateView(UpdateView):
    model = Station
    template_name = 'station/station_form.html'
    fields = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes', 'id_users']
    success_url = reverse_lazy('station:station_list')


class StationDeleteView(DeleteView):
    model = Station
    template_name = 'station/station_confirm_delete.html'
    success_url = reverse_lazy('station:station_list')
