from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cuve
def cuve_list(request):
    cuves = Cuve.objects.all()  
    return render(request, 'cuve/cuve_list.html', {'cuves': cuves})
class CuveListView(ListView):
    model = Cuve
    template_name = 'cuve/cuve_list.html'
    context_object_name = 'cuves'

class CuveCreateView(CreateView):
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    success_url = reverse_lazy('cuve:cuve_list')

class CuveUpdateView(UpdateView):
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    success_url = reverse_lazy('cuve:cuve_list')

class CuveDeleteView(DeleteView):
    model = Cuve
    template_name = 'cuve/cuve_confirm_delete.html'
    success_url = reverse_lazy('cuve:cuve_list')
