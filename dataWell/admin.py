from django.contrib import admin

from .models import RodPumpData, ESPData, ESPEvent

class confRPData(admin.ModelAdmin):
	list_display = ('PumpName','DateCreate','PumpFillDiagnosis', 'StatusDiagnosis')
	list_filter = ('StatusDiagnosis',)

admin.site.register(RodPumpData, confRPData)

class confESPData(admin.ModelAdmin):
	list_display = ('PumpName','DateCreate','MotorCurrent', 'MotorVoltage','MotorPower', 'MotorTemperature','MotorFrequency', 'HeadPressure','HeadTemperature','CasingPressure','FlowlinePressure','PumpIntakePressure')
	list_filter = ('PumpName',)

admin.site.register(ESPData, confESPData)

class confESPEvent(admin.ModelAdmin):
	list_display = ('PumpName','DateCreate','WellDiagnosis', 'FrequencySetPoint','TTT_under', 'TTT_over')
	list_filter = ('PumpName',)

admin.site.register(ESPEvent, confESPEvent)
