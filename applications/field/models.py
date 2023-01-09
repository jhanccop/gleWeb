from django.db import models
from applications.company.models import Company

from .managers import FieldManager

# Create your models here.
class Field(models.Model):
    DateCreated = models.DateTimeField(auto_now_add= True)
    FieldName = models.CharField('Field Name', max_length=100, unique=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, unique=False)
    LocationState = models.CharField('Location State', max_length=100)
    LocationCounty = models.CharField('Location County', max_length=100)

    objects = FieldManager()
    
    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'

    def __str__(self):
        #return '%s (%s)' % (self.PumpName,self.Available)
        return self.FieldName
        #return str(self.id)
