from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Cuve
from django.contrib import messages

from django.views.generic import ListView, CreateView, UpdateView

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
    model = Cuve
    template_name = 'cuve/cuve_form.html'
    fields = ['Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'id_station']
    success_url = reverse_lazy('cuve:cuve_list')

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
