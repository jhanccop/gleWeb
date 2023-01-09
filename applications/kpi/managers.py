from datetime import date, datetime

from django.db import models
from django.db.models import Count, Sum, Avg

class KPIManager(models.Manager):

    def list_deferement_by_field_interval(self, FieldName, intervalDate):
        Intervals = intervalDate.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]

        if len(intervals)==1:

            result = self.filter(
                    DateCreate__year=intervals[0].year,
                    DateCreate__month=intervals[0].month,
                    PumpName__FieldName__FieldName=FieldName
                ).values("PumpName__PumpName","PumpName__PumpType").annotate(
                    StopHours = Sum("StopHours"),
                    Deferment = Sum("Deferment")
                )
            return result
        else:
            result = self.filter(
                    DateCreate__range=(intervals[0],intervals[1]),
                    FieldName__FieldName=FieldName
                ).values("PumpName__PumpName","PumpName__PumpType").annotate(
                    StopHours = Sum("StopHours"),
                    Deferment = Sum("Deferment")
                )
            return result

    def list_deferement_by_field_month(self, FieldName):

        Today = date.today()

        result = self.filter(
            DateCreate__year=Today.year,
            DateCreate__month=Today.month,
            PumpName__FieldName__FieldName = FieldName,
            #FieldName__FieldName=FieldName
        ).values(
            "PumpName__PumpName",
            "PumpName__PumpType"
        ).annotate(
            StopHours = Sum("StopHours"),
            Deferment = Sum("Deferment")
        )
        return result

class FailuresManager(models.Manager):

    def list_runLife_by_field_month(self, FieldName):

        Today = date.today()

        result = self.filter(
            DateCreate__year=Today.year,
            DateCreate__month=Today.month,
            PumpName__FieldName__FieldName=FieldName
        ).values(
            "PumpName__PumpName",
            "PumpName__InstallationDate",
            #"DateFailure",
            #"FailureDiagnosis",
            #"PullOut",
        ).annotate(
            Count_failures = Count("PumpName__PumpName"),
            RunLife = Avg("RunLife")
        )

        # ************** optimizar para obtener ultimas lectura de cada pozo *******************
        result = list(result)
        print(result)
        for i in range(len(result)):
            last_values = self.filter(
                PumpName__PumpName=result[i]["PumpName__PumpName"]
            ).values(
                "DateFailure",
                "FailureDiagnosis",
                "PullOut"
            ).last()
            #print("---->",last_values)
            
            result[i].update(last_values)
        #print(result)
        return result

    def list_failues_by_field_month(self, CompanyName):

        Today = date.today()

        result = self.filter(
            DateCreate__year=Today.year,
            DateCreate__month=Today.month,
            PumpName__FieldName__Company=CompanyName
        ).values(
            "PumpName__FieldName__FieldName"
        ).annotate(
            CountFailures = Count("PumpName__FieldName__FieldName")
        )
        print(result)
        return result

    def search_last_failures(self, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).last()
        return result
