from django.contrib import admin

from .models import kpiData, failures

class confdeferment(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'
	list_display = ('PumpName','DateCreatedFormat', 'StopHours', 'Deferment')
	list_filter = ('PumpName',)

admin.site.register(kpiData, confdeferment)

class confFailures(admin.ModelAdmin):
	def DateCreatedFormat(self, obj):
		return obj.DateCreate.strftime("%Y-%m-%d %H:%M:%S")
	DateCreatedFormat.admin_order_field = 'DateCreated'
	DateCreatedFormat.short_description = 'Date Created'

	def DateFailureFormat(self, obj):
		return obj.DateFailure.strftime("%Y-%m-%d %H:%M:%S")
	DateFailureFormat.admin_order_field = 'DateFailure'
	DateFailureFormat.short_description = 'Date Failure'

	def PullOutFormat(self, obj):
		return obj.PullOut.strftime("%Y-%m-%d %H:%M:%S")
	PullOutFormat.admin_order_field = 'PullOut'
	PullOutFormat.short_description = 'Pull Out'

	list_display = ('PumpName','DateCreatedFormat','DateFailureFormat', 'FailureDiagnosis', 'PullOutFormat', 'RunLife')
	list_filter = ('PumpName','FailureDiagnosis')

admin.site.register(failures, confFailures)

# Register your models here.
