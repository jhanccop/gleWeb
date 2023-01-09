from django.db import models
from applications.well.models import well

# Create your models here.
class pvtTest(models.Model):
    DateCreated = models.DateTimeField(auto_now_add= True)
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, unique=False)
    
    # fluid properties
    APIGravity = models.FloatField('FP_API_Gravity', null=True, blank =True)
    BubblePointPressure = models.FloatField('FP_Bubble_Point_Pressure', null=True, blank =True)
    DynamicViscosity = models.FloatField('FP_Dynamic_Viscosity', null=True, blank =True)
    DewPoint = models.FloatField('FP_Dew_Point', null=True, blank =True)

    class Meta:
        verbose_name = 'PVT Test'
        verbose_name_plural = 'PVT Tests'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.PumpName
        #return str(self.id) + '-' + self.PumpName