from django.contrib import admin
from .models import well, completion, fluidProperties

class configWell(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('id','PumpName','PumpType','DateCreatedFormat','UserAuthor')
	list_filter = ( 'FieldName', 'PumpType','UserAuthor')

admin.site.register(well, configWell)

class configcompletion(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat','ESPumpType','MotorType','SaparatorType')
	list_filter = ( 'PumpName', 'ESPumpType','MotorType')

admin.site.register(completion, configcompletion)

class configfluidProperties(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat','API','Viscosity','BurblePoint','DewPoint')
	list_filter = ( 'PumpName',)

admin.site.register(fluidProperties, configfluidProperties)
