from django.db import models
from django.conf import settings

from applications.well.models import well
from multiselectfield import MultiSelectField

from .managers import EventManager, DataManager, WellTestManager, SampleTestManager, BuildUpTestManager, RPDataManager

class RodPumpData(models.Model):
    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)

    DateCreate = models.DateTimeField(auto_now_add= True, blank =True)
    LoadPump = models.TextField('Load',  null=True, blank =True)
    Position = models.TextField('Position', null=True, blank =True)
    Acceleration = models.TextField('Acceleration', null=True, blank =True)

    HeadPressure = models.FloatField('Head Pressure', null=True, blank =True)
    HeadTemperature = models.FloatField('Head Temperature', null=True, blank =True)
    CasingPressure = models.FloatField('Casing Pressure', null=True, blank =True)
    ChokeOpening= models.FloatField('Choke Opening', null=True, blank =True)
    SPM = models.FloatField('SPM', null=True, blank =True)

    DIAGNOSIS_CHOICES = (
        ('None', 'None'),
        ('Full pump', 'Full pump'),
        ('Leak travel valve', 'Leak travel valve'),
        ('Leak standing valve', 'Leak standing valve'),
        ('Worn pump barrel', 'Worn pump barrel'),
        ('Light fluid stroke', 'Light fluid stroke'),
        ('Medium fluid stroke', 'Medium fluid stroke'),
        ('Severe fluid stroke', 'Severe fluid stroke'),
        ('Gas interference', 'Gas interference'),
        ('Shock of pump up', 'Shock of pump up'),
        ('Shock of pump down', 'Shock of pump down'),
    )
    
    Diagnosis = MultiSelectField("Diagnosis", choices = DIAGNOSIS_CHOICES)
    PumpFill = models.FloatField('Pump Fill', null=True, blank =True)

    RECOMENDATION_CHOICES = (
        ('Good work area', 'Good work area'),
        ('Schedule to workover', 'Schedule to workover'),
        ('Unit re-spacing', 'Unit re-spacing'),
        ('Reduce strokes per minute', 'Reduce strokes per minute'),
        ('Stop pump unit', 'Stop pump unit'),
        ('Aply gle eliminator','Aply gle eliminator')
    )
    
    Recomendation = MultiSelectField("Recomendation", choices = RECOMENDATION_CHOICES)
    
    objects = RPDataManager()
    class Meta:
        verbose_name = 'Socker Rod Pump Data'
        verbose_name_plural = 'All Socker Rod Pump Data'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id) + '-' + self.PumpName

class ESPData(models.Model):

    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)
    DateCreate = models.DateTimeField(auto_now_add= True, blank =True)

    MotorCurrent = models.FloatField('Motor Current', null=True, blank =True)
    MotorVoltage = models.FloatField('Motor Voltage', null=True, blank =True)
    MotorPower  = models.FloatField('Motor Power', null=True, blank =True)
    MotorTemperature = models.FloatField('Motor Temperature', null=True, blank =True)
    MotorFrequency = models.FloatField('Motor Frequency', null=True, blank =True)
    HeadPressure = models.FloatField('Head Pressure', null=True, blank =True)
    HeadTemperature    = models.FloatField('Head Temperature', null=True, blank =True)
    CasingPressure = models.FloatField('Casing Pressure', null=True, blank =True)
    FlowlinePressure = models.FloatField('Flowline Pressure', null=True, blank =True)
    PumpIntakePressure = models.FloatField('Pump Intake Pressure', null=True, blank =True)

    objects = DataManager()

    class Meta:
        verbose_name = 'Electric Submersible Pump Data'
        verbose_name_plural = 'All Electric Submersible Pump Data'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)
        #return str(self.id) + '-' + self.PumpName

class ESPEvent(models.Model):

    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)
    DateCreate = models.DateTimeField(auto_now_add= False, blank =True)

    EVENT_CHOICES = (
        ("Normal Flow", "Normal Flow"),
        ("Pumping Off", "Pumping Off"),
        ("No Flow Condition", "No Flow Condition"),
        ("Broken Shaft", "Broken Shaft"),
        ("Off", "Off"),
        ("Abnormal flow", "Abnormal Off"),
        ("Flow Decreased", "Flow Decreased"),
        ("Flow Increased", "Flow Increased"),
    )
    WellEvent = models.CharField('Well Event', max_length=50, choices=EVENT_CHOICES, default="Normal Flow")

    DIAGNOSIS_CHOICES = (
        ("Normal", "Normal"),
        ("Gas Interference Traces", "Gas Interference Traces"),
        ("Gas Interference Light", "Gas Interference Light"),
        ("Gas Interference Medium", "Gas Interference Medium"),
        ("Gas Interference High", "Gas Interference High"),
        ("Gas Interference Severe", "Gas Interference Severe"),
        ("Gas Lock", "Gas Lock"),
        ("Gas Lock Severe", "Gas Lock Severe"),
    )
    WellDiagnosis = models.CharField('Well Diagnosis', max_length=50, choices=DIAGNOSIS_CHOICES, default="Normal Flow")

    WellPrediction = models.FloatField('Well Prediction', null=True, blank =True)
    EI = models.FloatField('E. I.', null=True, blank =True)
    WellRecomendation = models.CharField('Well Recomendation', max_length=50, null=True, blank =True)
    WellTripAttendant = models.CharField('Well Trip Attendant', max_length=50, null=True, blank =True)
    FrequencySetPoint = models.FloatField('Frequency SetPoint', null=True, blank =True)
    ChokeOpeningSetpoint = models.FloatField('Choke Opening Setpoint', null=True, blank =True)
    TTT = models.FloatField('Time To Trip', null=True, blank =True)

    objects = EventManager()

    class Meta:
        verbose_name = 'ESP Event'
        verbose_name_plural = 'ESP Events'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)

class WellTest(models.Model):

    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)
    DateCreate = models.DateTimeField(auto_now_add = True, blank = True)

    UserAuthor = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    DateStart = models.DateField(auto_now_add= False, blank =False)
    DateEnd = models.DateField(auto_now_add= False, blank =False)
    Duration = models.FloatField('Duration', null=True, blank =True)
    OilRate = models.FloatField('Oil Rate', null=True, blank =True)
    WaterRate = models.FloatField('Water Rate', null=True, blank =True)
    GasRate = models.FloatField('Gas Rate', null=True, blank =True)

    objects = WellTestManager()

    class Meta:
        verbose_name = 'Well Testing'
        verbose_name_plural = 'Well Testing'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)

class SampleTest(models.Model):

    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)
    DateCreate = models.DateTimeField(auto_now_add = True, blank =True)

    DateTest = models.DateTimeField(auto_now_add = False, blank =True)
    UserAuthor = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    WaterCut = models.FloatField('Water Cut', null=True, blank =True)
    SandPercentage = models.FloatField('Sand Percentage', null=True, blank =True)
    EmultionPercentage = models.FloatField('Emultion Percentage', null=True, blank =True)

    objects = SampleTestManager()

    class Meta:
        verbose_name = 'Sample Test'
        verbose_name_plural = 'Sample Test'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)

class BuildUpTest(models.Model):

    PumpName = models.ForeignKey(well, on_delete=models.CASCADE, null=False)
    DateCreate = models.DateTimeField(auto_now_add= True, blank =True)

    UserAuthor = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    DateStart = models.DateTimeField(auto_now_add= False, blank =True)
    DateEnd = models.DateTimeField(auto_now_add= False, blank =True)
    Duration = models.FloatField('Duration', null=True, blank =True)
    DataVector = models.CharField('Data Vector', max_length=50, null=True, blank =True)
    Permeability = models.FloatField('Permeability', null=True, blank =True)
    Skin = models.FloatField('Skin', null=True, blank =True)
    Iterated = models.FloatField('Iterated', null=True, blank =True)
    Extrapolated = models.FloatField('Extrapolated', null=True, blank =True)

    objects = BuildUpTestManager()

    class Meta:
        verbose_name = 'Build Up Test'
        verbose_name_plural = 'Build Up Test'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return str(self.PumpName)