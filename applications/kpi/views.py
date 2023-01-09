from unittest import result
from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from applications.field.models import Field
from applications.well.models import well
from applications.users.models import User
from applications.company.models import Company
from .models import kpiData, failures

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CompanyMixin(object):
    def get_context_data(self,**kwargs):
        company = User.objects.get_company_id(self.request.user)[0]["CompanyName"]
        company_name = Company.objects.get_company_name(company)[0]["CompanyName"]
        context = super(CompanyMixin,self).get_context_data(**kwargs)
        context['CompanyName'] = company_name
        return context

class ListFieldDeferment(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "kpi/deferment.html"
    login_url = reverse_lazy('user_app:user-login')
    
    def get_queryset(self):
        company_id = User.objects.get_company_id(self.request.user)[0]["CompanyName"]
        #company = Company.objects.get_company_name(company_id)[0]["CompanyName"]
        #company = self.kwargs['company']
        intervalDate = self.request.GET.get("dateKword", '')

        if intervalDate == "this month" or intervalDate == "This month" or intervalDate == "":
            list_fields = Field.objects.list_fields_by_companies(company_id)
            #result = {"company":company}
            result = {}
            allData = []
            for field_i in list_fields:
                temp = {
                    'FieldName':field_i["FieldName"]
                    #'company':company
                }
                list_fields = kpiData.objects.list_deferement_by_field_month(field_i["FieldName"])
                temp["list_fields"] = list_fields

                #print(list_fields)

                allData.append(temp)
            result["allData"] = allData
            return result
        else:
            list_fields = Field.objects.list_fields_by_companies(company_id)
            #result = {"company":company}
            result = {}
            allData = []
            for field_i in list_fields:
                temp = {
                    'FieldName':field_i["FieldName"]
                    #'company':company
                }
                list_fields = kpiData.objects.list_deferement_by_field_interval(field_i["FieldName"],intervalDate)
                temp["list_fields"] = list_fields

                print(list_fields)

                allData.append(temp)
            result["allData"] = allData
            return result
 
class ListFieldRunLife(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = "kpi/run-life.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        #company = self.kwargs['company']
        company_id = User.objects.get_company_id(self.request.user)[0]["CompanyName"]
        list_field = Field.objects.list_fields_by_companies(company_id)

        result = {}
        payload = []
        for Field_i in list_field:
            temp = {
                #"company":company,
                "FieldName":Field_i["FieldName"],
            }
            temp["data"] = failures.objects.list_runLife_by_field_month(Field_i["FieldName"])

            payload.append(temp)

        result["data"] = payload
        #print(payload)

        return result

class ListFieldFailureRate(LoginRequiredMixin, CompanyMixin, ListView):
    context_object_name = "list_failures"
    template_name = "kpi/failure-rate.html"
    login_url = reverse_lazy('user_app:user-login')

    def get_queryset(self):
        company_id = User.objects.get_company_id(self.request.user)[0]["CompanyName"]
        #company = self.kwargs['company']
        list_field = failures.objects.list_failues_by_field_month(company_id)

        result = {}
        result["data"] = list_field

        return result