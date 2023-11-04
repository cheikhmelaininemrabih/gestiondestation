from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pompiste
from django.urls import reverse_lazy

class PompisteListView(ListView):
    model = Pompiste
    template_name = 'pompiste_list.html'
    context_object_name = 'pompistes'

class PompisteCreateView(CreateView):
    model = Pompiste
    template_name = 'pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']
    def get_success_url(self):
        return reverse('pompiste_list')
class PompisteUpdateView(UpdateView):
    model = Pompiste
    template_name = 'pompiste_form.html'
    fields = ['Nom', 'Prenom', 'Adresse', 'tel', 'id_station']
    def get_success_url(self):
        return reverse('pompiste_list')
class PompisteDeleteView(DeleteView):
    model = Pompiste
    template_name = 'pompiste_confirm_delete.html'

    def get_success_url(self):
        return reverse('pompiste_confirm')