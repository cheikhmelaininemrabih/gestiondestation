from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Pompe
from rest_framework import viewsets
from .models import Pompe
from .serializers import PompeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PompeViewSet(viewsets.ModelViewSet):
    queryset = Pompe.objects.all()
    serializer_class = PompeSerializer

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
    def get(self, request, pk):
        pompe = get_object_or_404(Pompe, pk=pk)
        return render(request, self.template_name, {'pompe': pompe})

    
class PompeListView(APIView):
    """
    API view to retrieve a list of all active pompes.
    """
    def get(self, request):
        pompes = Pompe.objects.filter(is_active=True)
        serializer = PompeSerializer(pompes, many=True)
        return Response(serializer.data)




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