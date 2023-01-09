from datetime import date, datetime
from multiprocessing import context

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from applications.well.models import well, completion
from applications.kpi.models import failures
from applications.settings.models import setting
from .models import RodPumpData, ESPData, ESPEvent, WellTest, SampleTest, BuildUpTest
from applications.users.models import User
from applications.company.models import Company

from collections import Counter

from .forms import CreateWellTestForm

class CompanyMixin(object):
    def get_context_data(self,**kwargs):
        company = User.objects.get_company_id(self.request.user)[0]["CompanyName"]
        company_name = Company.objects.get_company_name(company)[0]["CompanyName"]
        context = super(CompanyMixin,self).get_context_data(**kwargs)
        context['CompanyName'] = company_name
        return context

class ListOverview(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/overview.html"
    login_url = reverse_lazy('user_app:user-login')
    #paginate_by = 2

    def get_queryset(self):
        #company = self.kwargs['company']
        company = User.objects.get_company_id(self.request.user)[0]["CompanyName"]

        list_wells = well.objects.filter(FieldName__Company__id=company, PumpType= "Electrical Submersible Pump")
        
        espData = []
        for well_i in list_wells:
            temp = {
                'PumpName':well_i.PumpName,
                'Field': well_i.FieldName,
            }

            settingWells = setting.objects.filter(PumpName=well_i).values("Available").last()
            if settingWells != None:
                temp['Available'] = settingWells["Available"]

            ESPDataList = ESPData.objects.filter(PumpName=well_i).last()
            if ESPDataList != None:
                    temp['MotorCurrent'] = ESPDataList.MotorCurrent
                    temp['MotorVoltage'] = ESPDataList.MotorVoltage
                    temp['MotorPower'] = ESPDataList.MotorPower
                    temp['MotorTemperature'] = ESPDataList.MotorTemperature
                    temp['MotorFrequency'] = ESPDataList.MotorFrequency
                    temp['HeadPressure'] = ESPDataList.HeadPressure
                    temp['HeadTemperature'] = ESPDataList.HeadTemperature
                    temp['CasingPressure'] = ESPDataList.CasingPressure
                    temp['FlowlinePressure'] = ESPDataList.FlowlinePressure
                    temp['PumpIntakePressure'] = ESPDataList.PumpIntakePressure
            
            EventDataList = ESPEvent.objects.filter(PumpName=well_i).last()

            if EventDataList != None:
                    temp['EI'] = EventDataList.EI
                    temp['WellEvent'] = EventDataList.WellEvent

            espData.append(temp)

        list_wells = well.objects.filter(FieldName__Company=company, PumpType= "Sucker Rod Pump")
        rodpumpData = []
        for well_i in list_wells:
            temp2 = {
                'PumpName':well_i.PumpName,
                'Field': well_i.FieldName,
            }

            settingWells = setting.objects.filter(PumpName=well_i).values("Available").last()
            if settingWells != None:
                temp2['Available'] = settingWells["Available"]

            dataWells2 = RodPumpData.objects.filter(PumpName=well_i).last()
            if dataWells2 != None:
                temp2['LastUpdate'] = dataWells2.DateCreate
                temp2['PIP'] = dataWells2.HeadPressure
                temp2['SPM'] = dataWells2.SPM
                temp2['PumpFill'] = dataWells2.PumpFill
                temp2['Diagnosis'] = dataWells2.Diagnosis
            
            rodpumpData.append(temp2)

        allData = {
            "espData":espData,
            "rodpumpData":rodpumpData
            }

        return allData

class ListDataRodPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/socked-rod-pump.html"
    login_url = reverse_lazy('user_app:user-login')
    #ordering = ['DateCreate']
    #paginate_by = 10

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        intervalDate = self.request.GET.get("dateKword", '')

        pump = well.objects.search_type_pump(wellName)

        if intervalDate == "today" or intervalDate == "Today" or intervalDate == "":
            list_data = RodPumpData.objects.search_today_RPata(wellName)
        else:
            list_data = RodPumpData.objects.search_by_interval_RPdata(intervalDate,wellName) #.order_by('-DateCreate')
        
        payload = {
            "name":wellName,
            "date":intervalDate,
            "type":pump["PumpType"],
            "data":list_data
            }
        
        return payload

class ListOperationDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-operation.html"
    login_url = reverse_lazy('user_app:user-login')
    #ordering = ['DateCreate']
    #paginate_by = 2

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        
        intervalDate = self.request.GET.get("dateKword", '')

        pumpType = well.objects.search_type_pump(wellName)

        if intervalDate == "today" or intervalDate == "Today" or intervalDate == "":
            list_event = ESPEvent.objects.search_today_event(intervalDate, wellName)
            list_data = ESPData.objects.search_today_data(intervalDate, wellName)
        else:
            list_event = ESPEvent.objects.search_by_interval_event(intervalDate, wellName)
            list_data = ESPData.objects.search_by_interval_data(intervalDate, wellName)

        payload = {
            "name":wellName,
            "date":intervalDate,
            "type":pumpType["PumpType"],
            "data":list_data,
            "event":list_event
            }
        
        return payload

class ListTrendsDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-trends.html"
    login_url = reverse_lazy('user_app:user-login')
    
    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        
        intervalDate = self.request.GET.get("dateKword", '')

        pumpType = well.objects.search_type_pump(wellName)

        if intervalDate == "today" or intervalDate == "Today" or intervalDate == "":
            list_event = ESPEvent.objects.search_today_event(intervalDate, wellName)
            list_data = ESPData.objects.search_today_data_all(intervalDate, wellName)
        else:
            list_event = ESPEvent.objects.search_by_interval_event(intervalDate, wellName)
            list_data = ESPData.objects.search_by_interval_data_all(intervalDate, wellName)

        payload = {
            "name":wellName,
            "date":intervalDate,
            "type":pumpType["PumpType"],
            "data":list_data,
            "event":list_event
            }
        
        return payload

class ListTroubleshootDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-troubleshoot.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        
        intervalDate = self.request.GET.get("dateKword", '')

        pumpType = well.objects.search_type_pump(wellName)

        if intervalDate == "today" or intervalDate == "Today" or intervalDate == "":
            list_event = ESPEvent.objects.search_today_event(intervalDate, wellName)
        else:
            list_event = ESPEvent.objects.search_by_interval_event(intervalDate, wellName)

        diagnosis = list_event.values("WellDiagnosis")
        list_diagnosis = [diag["WellDiagnosis"] for diag in diagnosis]

        counts = [list(Counter(list_diagnosis).keys()), list(Counter(list_diagnosis).values())]

        #print(counts)
        payload = {
            "name":wellName,
            "date":intervalDate,
            "type":pumpType["PumpType"],
            "count":counts,
            "event":list_event,
            }
        
        return payload

class ListOptimizationDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-optimization.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        
        pumpType = well.objects.search_type_pump(wellName)

        list_data = ESPData.objects.search_last_data(wellName)
        #list_completion = completion.objects.search_well_completion(wellName)
        list_event = ESPEvent.objects.search_last_event(wellName)
        list_failures = failures.objects.search_last_failures(wellName)

        payload = {
            "name":wellName,
            "type":pumpType["PumpType"],
            "data":list_data,
            #"completion":list_completion,
            "event":list_event,
            "failures":list_failures,
            }
        
        return payload

class ListTestDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-test.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
        intervalDate = self.request.GET.get("dateKword", '')

        if intervalDate == "all" or intervalDate == "All" or intervalDate == "":
            list_WellTest = WellTest.objects.search_by_all_WellTest(intervalDate, wellName)
            list_SampleTest = SampleTest.objects.search_by_all_SampleTest(intervalDate, wellName)
            list_BuildUpTest = BuildUpTest.objects.search_by_all_BuildUpTest(intervalDate, wellName)
        else:
            list_WellTest = WellTest.objects.search_by_intervals_WellTest(intervalDate, wellName)
            list_SampleTest = SampleTest.objects.search_by_intervals_SampleTest(intervalDate, wellName)
            list_BuildUpTest = BuildUpTest.objects.search_by_intervals_BuilUpTest(intervalDate, wellName)

        
        #list_SampleTest = SampleTest.objects.filter(PumpName__PumpName=wellName)
        #list_BuildUpTest = BuildUpTest.objects.filter(PumpName__PumpName=wellName)

        payload = {
            "name":wellName,
            "date":intervalDate,
            "WellTest":list_WellTest,
            "SampleTest":list_SampleTest,
            "BuildUpTest":list_BuildUpTest,
            }
        
        return payload

class ListInputDataESPump(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "overview/es-pump-input.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        wellName = self.kwargs['PumpName']
       
        payload = {
            "name":wellName,
            #"data":list_data,
            #"event":list_event,
            }
        
        return payload

class ListSmartAlarms(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "smartAlarms/smartAlarms.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        #wellName = self.kwargs['PumpName']
       
        payload = {
            "name":"welname",
            #"data":list_data,
            #"event":list_event,
            }
        
        return payload

class SuccessView(TemplateView):
    template_name = "home/home.html"

class CreateWellTestForm(LoginRequiredMixin,CreateView):
    template_name = "overview/create-well-test.html"
    login_url = reverse_lazy('user_app:user-login')

    model = WellTest
    form_class = CreateWellTestForm
    #fields = ('__all__')

    success_url = reverse_lazy('overview_app:overview')
    #success_url = reverse_lazy('overviews__applications:create_test')

