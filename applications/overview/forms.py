#from tkinter import Widget
from django import forms

from .models import WellTest

class CreateWellTestForm(forms.ModelForm):

    class Meta:

        model = WellTest
        fields = (
            "PumpName",
            "UserAuthor",
            "DateStart",
            "DateEnd",
            "Duration",
            "OilRate",
            "WaterRate",
            "GasRate",
        )

        widgets = {

            'PumpName': forms.Select(
                attrs = {
                    "class":"multisteps-form__select form-control text-center",
                    #"disabled":"true",
                    "required":"true",
                }
            ),

            'UserAuthor': forms.Select(
                attrs = {
                    "class":"multisteps-form__select form-control text-center",
                    #"disabled":"true",
                    "required":"true",
                    #"onfocus":"focused(this)",
                    #"onfocusout":"defocused(this)"
                }
            ),

            'DateStart': forms.DateInput(
                attrs = {
                    "class":"form-control datetimepicker text-center",
                    "type": "text",
                    #"onfocus":"focused(this)",
                    #"onfocusout":"defocused(this)"
                }
            ),

            'DateEnd': forms.DateInput(
                attrs = {
                    "class":"form-control datetimepicker text-center",
                    "type": "text"
                }
            ),

            'Duration': forms.NumberInput(
                attrs = {
                    'class' : 'form-control text-center',
                    "type":"number"
                }
            ),

            'OilRate': forms.NumberInput(
                attrs = {
                    'class' : 'form-control text-center',
                    "type":"number"
                }
            ),

            'WaterRate': forms.NumberInput(
                attrs = {
                    'class' : 'form-control text-center',
                    "type":"number"
                }
            ),
            
            'GasRate': forms.NumberInput(
                attrs = {
                    'class' : 'form-control text-center',
                    "type":"number"
                }
            ),
            
        }
