from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import StationSerializer
from .models import Station, Profile
from django import forms
from cuve.models import Cuve
from pompe.models import Pompe
from pompiste.models import Pompiste

class StationForm(forms.ModelForm):
    
    responsables = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.filter(role='responsable'),
        widget=forms.SelectMultiple,  
        required=False 
    )

    class Meta:
        model = Station
        fields = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes', 'responsables']

    def __init__(self, *args, **kwargs):
        super(StationForm, self).__init__(*args, **kwargs)
        self.fields['responsables'].label = "Responsable"





class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    cuves = Cuve.objects.filter(id_station=station)
    pompes = Pompe.objects.filter(id_cuve__in=cuves)
    pompistes = Pompiste.objects.filter(id_station=station)

    context = {
        'station': station,
        'station_id': pk,
        'cuves': cuves,
        'pompes': pompes,
        'pompistes': pompistes,
    }
    return render(request, 'station/station_detail.html', context)


class StationListView(ListView):
    model = Station
    template_name = 'station/station_list.html'
    context_object_name = 'stations'

    def get_queryset(self):
        return Station.objects.filter(is_active=True)

class StationCreateView(CreateView):
    model = Station
    form_class = StationForm  # Using custom form
    template_name = 'station/station_form.html'
    success_url = reverse_lazy('station:station_list')

class StationUpdateView(UpdateView):
    model = Station
    form_class = StationForm  # Using custom form
    template_name = 'station/station_form.html'
    success_url = reverse_lazy('station:station_list')

class StationDeactivateView(View):
    def post(self, request, pk):
        station = get_object_or_404(Station, pk=pk)
        station.is_active = False
        station.save()
        return redirect(reverse_lazy('station:station_list'))
