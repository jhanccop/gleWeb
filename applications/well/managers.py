from django.db import models

class WellManager(models.Manager):

    def search_type_pump(self, wellName):
        result = self.filter(
            PumpName=wellName
        ).values("PumpType")
        return result[0]

class CompletionManager(models.Manager):

    def search_well_completion(self, wellName):
        result = self.filter(
            PumpName__PumpName=wellName
        ).last()
        return result