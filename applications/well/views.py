from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from .models import well
from applications.overview.models import RodPumpData, ESPData

# Create your views here.
class ListWellsCompany(ListView):
    template_name = "overview/overview.html"

    def get_queryset(self):
        company = self.kwargs['company']
        allData = []

        list_wells = well.objects.filter(Company=company, PumpType= "Electric Submersible Pump")
        espData = []
        for well_i in list_wells:
            dataWells = ESPData.objects.filter(PumpName=well_i).last()
            temp = {
                'PumpName':well_i.PumpName,
                'Field': well_i.Field,

                'MotorCurrent': dataWells.MotorCurrent,
                'MotorVoltage':dataWells.MotorVoltage,
                'MotorPower':dataWells.MotorPower,
                'MotorTemperature':dataWells.MotorTemperature,
                'MotorFrequency':dataWells.MotorFrequency,
                'HeadPressure': dataWells.HeadPressure,
                'HeadTemperature':dataWells.HeadTemperature,
                'CasingPressure':dataWells.CasingPressure,
                'FlowlinePressure':dataWells.FlowlinePressure,
                'PumpIntakePressure':dataWells.PumpIntakePressure,
                }
            espData.append(temp)

        list_wells = well.objects.filter(Company=company, PumpType= "Sucker Rod Pump")
        rodpumpData = []
        for well_i in list_wells:
            dataWells = RodPumpData.objects.filter(PumpName=well_i).last()
            temp = {
                'PumpName':well_i.PumpName,
                'Field': well_i.Field,
                'LastUpdate': dataWells.DateCreate,
                
                'PIP':dataWells.HeadPressure,
                'SPM':dataWells.RPM,
                'PumpFill':dataWells.PumpFill,
                'Diagnosis':dataWells.StatusDiagnosis,
                }
            rodpumpData.append(temp)

        allData = [espData, rodpumpData]

        return allData