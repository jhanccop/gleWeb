# Generated by Django 3.2 on 2022-10-18 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CompanyName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
