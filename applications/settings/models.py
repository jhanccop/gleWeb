from django.db import models

from applications.well.models import well

# Create your models here.
class setting(models.Model):

    DateCreated = models.DateTimeField(auto_now_add= True)
    PumpName = models.OneToOneField(well, on_delete=models.CASCADE,null=False, blank=False)
  
    # Operational information
    Available = models.BooleanField('Available',default=True)
    IpAddress = models.CharField('Ip Address', max_length=100, unique=True)
    
    # control information
    CONTROL_CHOICES = (
        ("None", "None"),
        ("Amperage", "Amperage"),
        ("Frequency", "Frequency"),
    )
    ControlMode = models.CharField('Control Mode', max_length=10, choices=CONTROL_CHOICES, default="None")
    ControlSetPoint =  models.FloatField('Control SetPoint', null=True, blank =True)
    ControlSetPointChokeValve =  models.FloatField('SetPoint ChokeValve', null=True, blank =True)
