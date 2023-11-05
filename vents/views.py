from django.shortcuts import render, redirect
from .models import Vente
from .forms import VenteForm

def create_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST, request.FILES)
        if form.is_valid():
            new_vente = form.save()
            
            return redirect('vente:vente_list')
    else:
        form = VenteForm()
    return render(request, 'vente/create_vente.html', {'form': form})
