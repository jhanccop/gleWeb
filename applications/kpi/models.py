from django.db import models
from applications.field.models import Field
from applications.well.models import well

from .managers import KPIManager, FailuresManager

# Create your models here.
class kpiData(models.Model):
    
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False,related_name='well_kpi')
    DateCreate = models.DateTimeField(auto_now_add= True)
    #FieldName = models.ForeignKey(Field, on_delete=models.CASCADE, null=False)
    
    StopHours = models.FloatField('Stop Hours', null=True, blank =True)
    Deferment = models.FloatField('Deferment', null=True, blank =True)

    RunLife = models.FloatField('Run Life', null=True, blank =True)

    objects = KPIManager()
    class Meta:
        verbose_name = 'deferment'
        verbose_name_plural = 'deferment'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id)

class failures(models.Model):
    
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False,related_name='well_failures')
    DateCreate = models.DateTimeField(auto_now_add= True)
    #FieldName = models.ForeignKey(Field, on_delete=models.CASCADE, null=False,related_name='Field_failures')

    DateFailure = models.DateTimeField(auto_now_add= False, blank =False)
    FailureDiagnosis = models.CharField('Failure Diagnosis', max_length=50, null=True, blank =True)
    PullOut = models.DateTimeField(auto_now_add= False, blank =False)
    RunLife = models.FloatField('Run Life', null=True, blank =True)

    objects = FailuresManager()

    class Meta:
        verbose_name = 'failures'
        verbose_name_plural = 'failures'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id)
