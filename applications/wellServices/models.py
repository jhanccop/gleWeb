from django.db import models

# Create your models here.

class TypesRodPump(models.Model):
    TYPES_CHOICES = (
        ("Other", "Other"),
        ("Conventional Unit", "Conventional Unit"),
        ("Mark II Unit", "Mark II Unit"),
        ("Reverse Mark Pumping Unit", "Reverse Mark Pumping Unit"),
        ("Air Balanced Pumping Unit", "Air Balanced Pumping Unit"),
        ("Low Profile Pumping Unit", "Low Profile Pumping Unit"),
        ("Beam Balanced Unit", "Beam Balanced Unit"),
        ("Hydraulic Pumping Unit", "Hydraulic Pumping Unit"),
        ("Long Stroke Belt Driven Unit", "Long Stroke Belt Driven Unit"),
        ("Hydraulic Cable Driven Unit", "Hydraulic Cable Driven Unit"),
        ("Linear Rod Pumping Unit", "Linear Rod Pumping Unit"),
    )
    choice = models.CharField('TypeRodPump',max_length=50, choices=TYPES_CHOICES, default="Conventional Unit")

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.choice
        #return str(self.id) + '-' + self.PumpName

class RodPumpInstallation(models.Model):
    DateCreated = models.DateTimeField(auto_now_add= True)
    PumpName = models.CharField('Pump_Name', max_length=100, unique=True)
    ServiceCompany = models.CharField('Service_Company', max_length=100)
    StartDateTime = models.DateTimeField(auto_now_add = False, default=True)
    EndDateTime = models.DateTimeField(auto_now_add = False, default=True)

    # surface installation information
    PipeDiameter =  models.FloatField('Pipe_Diameter', null=True, blank =True)
    TypeRodPump = models.OneToOneField(TypesRodPump, on_delete=models.CASCADE)
    APIRodPumpDesignation = models.FloatField('API_Rod_Pump_Designation', null=True, blank =True)

    # electrical installation information
    MotorType = models.CharField('Motor_Type', max_length=100, null=True, blank =True)
    MotorBrand = models.CharField('Motor_Brand', max_length=100, null=True, blank =True)
    MotorPower = models.FloatField('Motor_Power', null=True, blank =True)
    MotorCurrent = models.FloatField('Motor_Current', null=True, blank =True)
    MotorCUL = models.FloatField('Motor_CUL', null=True, blank =True)
    MotorCOL = models.FloatField('Motor_COL', null=True, blank =True)
    MotorVoltaje = models.FloatField('Motor_Voltaje', null=True, blank =True)
    MotorVUL = models.FloatField('Motor_VUL', null=True, blank =True)
    MotorVOL = models.FloatField('Motor_VOL', null=True, blank =True)
    MotorFrequency = models.FloatField('Motor_Frequency', null=True, blank =True)
    MotorMaxFrequency = models.FloatField('Motor_Max_Frequency', null=True, blank =True)
    MotorMinFrequency = models.FloatField('Motor_Min_Frequency', null=True, blank =True)
    MotorGroundFault =  models.FloatField('Motor_Ground_Fault', null=True, blank =True)

    # downhole installation information
    TubingDiameter = models.FloatField('Tubing_Diameter', null=True, blank =True)
    CasingDiameter = models.FloatField('Casing_Diameter', null=True, blank =True)
    PumpType = models.CharField('Pump_Type', max_length=100, null=True, blank =True)
    PumpDepth =  models.FloatField('Pump_Depth', null=True, blank =True)
    APIpumpsDesignation = models.FloatField('API_pumps_Designation', null=True, blank =True)
    PumpEfficiency =  models.FloatField('Pump_Efficiency', null=True, blank =True)
    SeparatorType = models.CharField('Separator_Type', max_length=100, null=True, blank =True)
    SeparatorEfficiency =  models.FloatField('Separator_Efficiency', null=True, blank =True)

    class Meta:
        verbose_name = 'Rod Pump Installation'
        verbose_name_plural = 'Rod Pump Installations'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.PumpName
        #return str(self.id) + '-' + self.PumpName

class ESPInstallation(models.Model):
    DateCreated = models.DateTimeField(auto_now_add= True)
    PumpName = models.CharField('Pump_Name', max_length=100, unique=True)
    ServiceCompany = models.CharField('Service_Company', max_length=100)
    StartDateTime = models.DateTimeField(auto_now_add = False, default=True)
    EndDateTime = models.DateTimeField(auto_now_add = False, default=True)

     # electrical installation information
    TransformerInputVoltage = models.FloatField('Transformer_Input_Voltage', null=True, blank =True)
    TransformerOutputVoltage= models.FloatField('Transformer_Output_Voltage', null=True, blank =True)
    PumpType = models.CharField('Pump_Type', max_length=500, default=True)
    PumpStageType = models.BigIntegerField('Pump_Stage_Type',default=True)
    PumpDownthrustFlow = models.FloatField('Pump_Downthrust_Flow', null=True, blank =True)
    PumpUpthrustFlow = models.FloatField('Pump_Upthrust_Flow', null=True, blank =True)
    PumpSetDepth = models.FloatField('Pump_Set_Depth', null=True, blank =True)
    PumpNumberOfStages = models.BigIntegerField('Pump_Number_Of_Stages',default=True)
    PumpBestEfficiencyPoint = models.FloatField('Pump_Best_Efficiency_Point', null=True, blank =True)
    MotorType = models.CharField('Motor_Type', max_length=100, default=True)
    MotorTemperatureResistance = models.BigIntegerField('Motor_Temperature_Resistance',default=True)
    MotorNominalCurrent = models.FloatField('Motor_Nominal_Current', null=True, blank =True)
    MotorNominalVoltage = models.FloatField('Motor_Nominal_Voltage', null=True, blank =True)
    MotorNominalPower = models.FloatField('Motor_Nominal_Power', null=True, blank =True)
    MotorNominalFrequency = models.FloatField('Motor_Nominal_Frequency', null=True, blank =True)
    SeparatorType = models.CharField('Separator_Type', max_length=100, null=True, blank =True)
    SeparatorEfficiency =  models.FloatField('Separator_Efficiency', null=True, blank =True)

    # downhole installation information
    TubingDiameter = models.FloatField('Tubing_Diameter', null=True, blank =True)
    CasingDiameter = models.FloatField('Casing_Diameter', null=True, blank =True)
    LinerDiameter = models.FloatField('Liner_Diameter', null=True, blank =True)
    TubingDepth = models.FloatField('Tubing_Depth', null=True, blank =True)
    CasingDepth = models.FloatField('Casing_Depth', null=True, blank =True)
    LinerDepth = models.FloatField('Liner_Depth', null=True, blank =True)

    class Meta:
            verbose_name = 'ESP Installation'
            verbose_name_plural = 'ESP Installations'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.PumpName
        #return str(self.id) + '-' + self.PumpName