from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Pompiste

class PompisteListView(ListView):
    model = Pompiste
    template_name = 'pompiste/pompiste_list.html'
    context_object_name = 'pompistes'
    def get_queryset(self):
        return Pompiste.objects.filter(is_active=True)
class PompisteCreateView(CreateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']

    def get_success_url(self):
        return reverse_lazy('pompiste:pompiste_list')

class PompisteUpdateView(UpdateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']

    def get_success_url(self):
        return reverse_lazy('pompiste:pompiste_list')

class PompisteDeactivateView(TemplateView):
    template_name = 'pompiste/pompiste_desactivate.html'

    def post(self, request, pk):
        pompiste = get_object_or_404(Pompiste, pk=pk)
        pompiste.is_active = False
        pompiste.save()
        return redirect(reverse_lazy('pompiste:pompiste_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pompiste'] = get_object_or_404(Pompiste, pk=self.kwargs['pk'])
        return context