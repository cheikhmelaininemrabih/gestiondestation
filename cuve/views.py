from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Cuve
from django.contrib import messages
from station.models import Station
from django.views.generic.edit import CreateView
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework import viewsets
from .serializers import CuveSerializer

class CuveViewSet(viewsets.ModelViewSet):
    queryset = Cuve.objects.all()
    serializer_class = CuveSerializer

class CuveListByStationView(ListView):
    model = Cuve
    template_name = 'cuve/cuve_list.html'
    context_object_name = 'cuves'

    def get_queryset(self):
        station_id = self.kwargs.get('station_id')
        return Cuve.objects.filter(id_station_id=station_id)
    
    def get_context_data(self, **kwargs):
        context = super(CuveListByStationView, self).get_context_data(**kwargs)
        context['station_id'] = self.kwargs['station_id']  # Pass the station ID to the template
        return context
    



def cuve_list(request):
    cuves = Cuve.objects.all()  
    return render(request, 'cuve/cuve_list.html', {'cuves': cuves})
class CuveListView(ListView):
    model = Cuve
    template_name = 'cuve/cuve_list.html'
    context_object_name = 'cuves'
    def get_queryset(self):
        return Cuve.objects.all()



class CuveCreateView(CreateView):
    model = Cuve  # Ensure this line is correct and 'Cuve' is properly imported
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']

    def form_valid(self, form):
        # Convert the 'station_id' URL parameter to an actual Station instance
        station_id = self.kwargs.get('station_id')
        form.instance.id_station = get_object_or_404(Station, pk=station_id)
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the cuve list for the specific station
        station_id = self.object.id_station.id
        return reverse_lazy('cuve:cuve_list_for_station', kwargs={'station_id': station_id})




class CuveUpdateView(UpdateView):
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    success_url = reverse_lazy('cuve:cuve_list')

class CuveDeactivateView(View):
    template_name = 'cuve/cuve_desactivate.html'

    def get(self, request, pk):
        cuve = get_object_or_404(Cuve, pk=pk)
        return render(request, self.template_name, {'cuve': cuve})

    def post(self, request, pk):
        cuve = get_object_or_404(Cuve, pk=pk)
        cuve.is_active = False
        cuve.save()
        messages.success(request, f'Cuve {cuve.id} has been successfully deactivated.')
        return redirect(reverse_lazy('cuve:cuve_list'))
class CuveReactivateView(View):
    template_name = 'cuve/cuve_reactivate_confirm.html'

    def get(self, request, pk):
        cuve = get_object_or_404(Cuve, pk=pk)
        return render(request, self.template_name, {'cuve': cuve})

    def post(self, request, pk):
        cuve = get_object_or_404(Cuve, pk=pk)
        cuve.is_active = True
        cuve.save()
        messages.success(request, f'Cuve {cuve.id} has been successfully reactivated.')
        return redirect(reverse_lazy('cuve:cuve_list'))
