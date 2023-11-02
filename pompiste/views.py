from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pompiste
from django.urls import reverse_lazy

class PompisteListView(ListView):
    model = Pompiste
    template_name = 'pompiste/pompiste_list.html'
    context_object_name = 'pompistes'

class PompisteCreateView(CreateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']
    success_url = reverse_lazy('pompiste_list')

class PompisteUpdateView(UpdateView):
    model = Pompiste
    template_name = 'pompiste/pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']
    success_url = reverse_lazy('pompiste_list')

class PompisteDeleteView(DeleteView):
    model = Pompiste
    template_name = 'pompiste/pompiste_confirm_delete.html'
    success_url = reverse_lazy('pompiste_list')
