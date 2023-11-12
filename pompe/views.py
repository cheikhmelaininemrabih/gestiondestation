from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Pompe

class PompeListView(ListView):
    model = Pompe
    template_name = 'pompe_list.html'
    context_object_name = 'pompes'
    def get_queryset(self):
       
        return Pompe.objects.filter(is_active=True)

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




class PompeDeactivateView(View):
    template_name = 'pompe/pompe_desactivate.html'

    def get(self, request, pk):
        pompe = get_object_or_404(Pompe, pk=pk)
        return render(request, self.template_name, {'pompe': pompe})

    def post(self, request, pk):
        pompe = get_object_or_404(Pompe, pk=pk)
        pompe.is_active = False
        pompe.save()
        messages.success(request, f'Pompe {pompe.type} has been successfully deactivated.')
        return redirect(reverse_lazy('pompe:pompe_list'))
class PompeReactivateView(View):
    template_name = 'pompe/pompe_reactivate_confirm.html'

    def get(self, request, pk):
        cuve = get_object_or_404(Pompe, pk=pk)
        return render(request, self.template_name, {'pompe': Pompe})

    def post(self, request, pk):
        cuve = get_object_or_404(Pompe, pk=pk)
        cuve.is_active = True
        cuve.save()
        messages.success(request, f'Pompe {Pompe.id} has been successfully reactivated.')
        return redirect(reverse_lazy('pompe:pompe_list'))
