from django.shortcuts import render
from datetime import date, datetime

from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from applications.well.models import well
from .models import RodPumpData, ESPData

class ListRodPump(ListView):
    template_name = "dataWell/rod-pump.html"

    def get_queryset(self):
        well = self.kwargs['PumpName']
        list_wells = RodPumpData.objects.filter(PumpName__PumpName=well).order_by('-DateCreate')
        return list_wells

class ListESPump(ListView):
    template_name = "dataWell/es-pump.html"

    def get_queryset(self):
        well = self.kwargs['PumpName']
        #,DateCreate=datetime.today().date()
        today = date.today()
        list_wells = ESPData.objects.filter(DateCreate__year=today.year, DateCreate__month=today.month, DateCreate__day=today.day,PumpName__PumpName=well).order_by('-DateCreate')
        
        
        context = [well, list_wells]
        print(context)
        #context['name'] = well
        #context['msg'] = list_wells
        return context


