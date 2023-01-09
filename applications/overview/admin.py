from django.contrib import admin

# Register your models here.
#from django.contrib import admin

from .models import RodPumpData, ESPData, ESPEvent, WellTest, SampleTest, BuildUpTest

class confRPData(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created' 
	list_display = ('PumpName','DateCreatedFormat','PumpFill', 'Diagnosis','Recomendation')
	list_filter = ('Diagnosis',)
admin.site.register(RodPumpData, confRPData)

class confESPData(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat','MotorCurrent', 'MotorVoltage','MotorPower', 'MotorTemperature','MotorFrequency', 'HeadPressure','HeadTemperature','CasingPressure','FlowlinePressure','PumpIntakePressure')
	list_filter = ('PumpName',)
admin.site.register(ESPData, confESPData)

class confESPEvent(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat','WellDiagnosis',"WellEvent",'WellRecomendation','EI','WellTripAttendant','FrequencySetPoint','ChokeOpeningSetpoint')
	list_filter = ('PumpName',)
admin.site.register(ESPEvent, confESPEvent)

class confWellTest(admin.ModelAdmin):
	def DateStartFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d")
	DateStartFormat.admin_order_field = 'DateCreated'
	DateStartFormat.short_description = 'Date Created'

	def DateEndFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d")
	DateEndFormat.admin_order_field = 'DateCreated'
	DateEndFormat.short_description = 'Date Created'
	list_display = ('PumpName','UserAuthor','DateStartFormat','DateEndFormat','Duration','OilRate','WaterRate','GasRate')
	list_filter = ('PumpName',)
admin.site.register(WellTest, confWellTest)

class confSampleTest(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat','UserAuthor','WaterCut','SandPercentage','EmultionPercentage')
	list_filter = ('PumpName',)

admin.site.register(SampleTest, confSampleTest)

class confBuildUpTest(admin.ModelAdmin):
	def DateStartFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d")
	DateStartFormat.admin_order_field = 'DateCreated'
	DateStartFormat.short_description = 'Date Created'

	def DateEndFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d")
	DateEndFormat.admin_order_field = 'DateCreated'
	DateEndFormat.short_description = 'Date Created'
	list_display = ('PumpName','UserAuthor','DateStartFormat','DateEndFormat','Duration','DataVector','Permeability','Skin','Iterated','Extrapolated')
	list_filter = ('PumpName',)

admin.site.register(BuildUpTest, confBuildUpTest)
