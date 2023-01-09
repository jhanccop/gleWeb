from django.contrib import admin
from .models import setting

class configSettings(admin.ModelAdmin):
	list_display = ('DateCreated', 'PumpName', 'Available', 'IpAddress', 'ControlMode', 'ControlSetPoint', 'ControlSetPointChokeValve')
	list_filter = ('Available', 'ControlMode')

admin.site.register(setting, configSettings)