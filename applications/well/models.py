from wsgiref.handlers import format_date_time
from django.db import models
from django.conf import settings

from applications.field.models import Field
#from applications.company.models import Company

from .managers import WellManager, CompletionManager

class well(models.Model):

    # General information
    DateCreate = models.DateTimeField(auto_now_add= True )
    PumpName = models.CharField('Pump Name', max_length=100, unique=True)
    #Company = models.ForeignKey(Company, on_delete=models.CASCADE, unique=False)
    FieldName = models.ForeignKey(Field, on_delete=models.CASCADE, unique=False)
    Location = models.CharField('Location', max_length=100)
    UserAuthor = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    InstallationDate = models.DateField(auto_now_add = False)
    InstallationComment = models.TextField('Installation Comment', max_length=500)
    
    # type well
    TYPE_CHOICES = (
        ("Sucker Rod Pump", "Sucker Rod Pump"),
        ("Electrical Submersible Pump", "Electrical Submersible Pump"),
    )
    PumpType = models.CharField('Pump Type', max_length=50, choices=TYPE_CHOICES, default="Sucker Rod Pump")

    objects = WellManager()
    class Meta:
        verbose_name = 'well'
        verbose_name_plural = 'wells'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.PumpName
        #return str(self.id) + '-' + self.PumpName

class completion(models.Model):
    
    # General information
    DateCreate = models.DateTimeField(auto_now_add= True)
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)

    # Suface Equipment
    TransformerInputVoltage = models.FloatField('Transformer Input Voltage', null=True, blank =True)
    TransformerOutputVoltage = models.FloatField('Transformer Output Voltage', null=True, blank =True)
    TransformerPower = models.FloatField('Transformer Power', null=True, blank =True)
    AmbientTemperature = models.FloatField('Ambient Temperature', null=True, blank =True)

    # Pump
    ESPumpType = models.CharField('ES Pump Type', max_length=100)

    TYPE_CHOICES = (
        ("Floating type", "Floating type"),
        ("Compression type", "Compression type"),
    )
    StateType = models.CharField('State Type', max_length=50, choices=TYPE_CHOICES, default="Floating type")
    Downthrust = models.FloatField('Downthrust', null=True, blank =True)
    Upthrust = models.FloatField('Upthrust', null=True, blank =True)
    SetDepth = models.FloatField('Set Depth', null=True, blank =True)
    NumberOfStages = models.FloatField('Number Of Stages', null=True, blank =True)
    BestEfficiencyPoint = models.FloatField('Best Efficiency Point', null=True, blank =True)

    # Motor
    MotorType = models.CharField('Motor Type', max_length=100)
    NominalCurrent = models.FloatField('Motor Nominal Current', null=True, blank =True)
    NominalFrequency = models.FloatField('Motor Nominal Frequency', null=True, blank =True)

    TYPE_CHOICES = (
        ("Standard", "Standard"),
        ("Intermediate", "Intermediate"),
        ("High Temperature", "High Temperature"),
    )
    TemperatureResistance = models.CharField('Temperature Resistance', max_length=50, choices=TYPE_CHOICES, default="Standard")
    NominalVoltage = models.FloatField('Nominal Voltaget', null=True, blank =True)
    NominalPower = models.FloatField('Nominal Power', null=True, blank =True)
    IdleCurrent = models.FloatField('Idle Current', null=True, blank =True)

    # downHole installation
    TubingDiameter = models.FloatField('Tubing Diametert', null=True, blank =True)
    CasingDiameter = models.FloatField('Casing Diameter', null=True, blank =True)
    LinerDiameter = models.FloatField('Liner Diameter', null=True, blank =True)
    TubingDepth = models.FloatField('Tubing Depth', null=True, blank =True)
    CasingDepth = models.FloatField('Casing Depth', null=True, blank =True)
    LinerDepth = models.FloatField('Liner Depth', null=True, blank =True)

     # Separator
    TYPE_CHOICES = (
        ("Standard", "Standard"),
        ("Enhanced", "Enhanced"),
        ("Advanced", "Advanced"),
    )
    SaparatorType = models.CharField('Separator Type', max_length=50, choices=TYPE_CHOICES, default="Standard")

    objects = CompletionManager()

    class Meta:
        verbose_name = 'completion'
        verbose_name_plural = 'completion'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id) + '-' + self.PumpName

class fluidProperties(models.Model):
    DateCreate = models.DateTimeField(auto_now_add= True)
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)

    API = models.FloatField('API', null=True, blank =True)
    Viscosity = models.FloatField('Viscosity', null=True, blank =True)
    BurblePoint = models.FloatField('Burble Point', null=True, blank =True)
    DewPoint = models.FloatField('Dew Point', null=True, blank =True)

    class Meta:
        verbose_name = 'Fluid Properties'
        verbose_name_plural = 'Fluid Properties'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id) + '-' + self.PumpName
