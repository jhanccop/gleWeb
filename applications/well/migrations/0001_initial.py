# Generated by Django 3.2 on 2022-10-18 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreate', models.DateTimeField(auto_now_add=True)),
                ('PumpName', models.CharField(max_length=100, unique=True, verbose_name='Pump Name')),
                ('Company', models.CharField(max_length=100, verbose_name='Company')),
                ('Location', models.CharField(max_length=100, verbose_name='Location')),
                ('InstallationDate', models.DateField()),
                ('InstallationComment', models.TextField(max_length=500, verbose_name='Installation Comment')),
                ('PumpType', models.CharField(choices=[('Sucker Rod Pump', 'Sucker Rod Pump'), ('Electrical Submersible Pump', 'Electrical Submersible Pump')], default='Sucker Rod Pump', max_length=50, verbose_name='Pump Type')),
                ('FieldName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='field.field')),
                ('UserAuthor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'well',
                'verbose_name_plural': 'wells',
            },
        ),
        migrations.CreateModel(
            name='fluidProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreate', models.DateTimeField(auto_now_add=True)),
                ('API', models.FloatField(blank=True, null=True, verbose_name='API')),
                ('Viscosity', models.FloatField(blank=True, null=True, verbose_name='Viscosity')),
                ('BurblePoint', models.FloatField(blank=True, null=True, verbose_name='Burble Point')),
                ('DewPoint', models.FloatField(blank=True, null=True, verbose_name='Dew Point')),
                ('PumpName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='well.well')),
            ],
            options={
                'verbose_name': 'Fluid Properties',
                'verbose_name_plural': 'Fluid Properties',
            },
        ),
        migrations.CreateModel(
            name='completion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreate', models.DateTimeField(auto_now_add=True)),
                ('TransformerInputVoltage', models.FloatField(blank=True, null=True, verbose_name='Transformer Input Voltage')),
                ('TransformerOutputVoltage', models.FloatField(blank=True, null=True, verbose_name='Transformer Output Voltage')),
                ('TransformerPower', models.FloatField(blank=True, null=True, verbose_name='Transformer Power')),
                ('AmbientTemperature', models.FloatField(blank=True, null=True, verbose_name='Ambient Temperature')),
                ('ESPumpType', models.CharField(max_length=100, verbose_name='ES Pump Type')),
                ('StateType', models.CharField(choices=[('Floating type', 'Floating type'), ('Compression type', 'Compression type')], default='Floating type', max_length=50, verbose_name='State Type')),
                ('Downthrust', models.FloatField(blank=True, null=True, verbose_name='Downthrust')),
                ('Upthrust', models.FloatField(blank=True, null=True, verbose_name='Upthrust')),
                ('SetDepth', models.FloatField(blank=True, null=True, verbose_name='Set Depth')),
                ('NumberOfStages', models.FloatField(blank=True, null=True, verbose_name='Number Of Stages')),
                ('BestEfficiencyPoint', models.FloatField(blank=True, null=True, verbose_name='Best Efficiency Point')),
                ('MotorType', models.CharField(max_length=100, verbose_name='Motor Type')),
                ('NominalCurrent', models.FloatField(blank=True, null=True, verbose_name='Motor Nominal Current')),
                ('NominalFrequency', models.FloatField(blank=True, null=True, verbose_name='Motor Nominal Frequency')),
                ('TemperatureResistance', models.CharField(choices=[('Standard', 'Standard'), ('Intermediate', 'Intermediate'), ('High Temperature', 'High Temperature')], default='Standard', max_length=50, verbose_name='Temperature Resistance')),
                ('NominalVoltage', models.FloatField(blank=True, null=True, verbose_name='Nominal Voltaget')),
                ('NominalPower', models.FloatField(blank=True, null=True, verbose_name='Nominal Power')),
                ('IdleCurrent', models.FloatField(blank=True, null=True, verbose_name='Idle Current')),
                ('TubingDiameter', models.FloatField(blank=True, null=True, verbose_name='Tubing Diametert')),
                ('CasingDiameter', models.FloatField(blank=True, null=True, verbose_name='Casing Diameter')),
                ('LinerDiameter', models.FloatField(blank=True, null=True, verbose_name='Liner Diameter')),
                ('TubingDepth', models.FloatField(blank=True, null=True, verbose_name='Tubing Depth')),
                ('CasingDepth', models.FloatField(blank=True, null=True, verbose_name='Casing Depth')),
                ('LinerDepth', models.FloatField(blank=True, null=True, verbose_name='Liner Depth')),
                ('SaparatorType', models.CharField(choices=[('Standard', 'Standard'), ('Enhanced', 'Enhanced'), ('Advanced', 'Advanced')], default='Standard', max_length=50, verbose_name='Separator Type')),
                ('PumpName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='well.well')),
            ],
            options={
                'verbose_name': 'completion',
                'verbose_name_plural': 'completion',
            },
        ),
    ]
