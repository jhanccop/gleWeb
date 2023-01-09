from datetime import date, datetime

from unittest import result
from django.db import models

class EventManager(models.Manager):

    def search_by_interval_event(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_today_event(self, interval, wellName):
        Today = date.today()
        result = self.filter(
                DateCreate__year=Today.year,
                DateCreate__month=Today.month,
                DateCreate__day=Today.day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
        return result

    def search_last_event(self, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).last()
        return result

class DataManager(models.Manager):
    def search_by_interval_data(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).values("DateCreate","MotorCurrent","HeadPressure","MotorFrequency").order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_today_data(self, interval, wellName):
        Today = date.today()
        result = self.filter(
                DateCreate__year=Today.year,
                DateCreate__month=Today.month,
                DateCreate__day=Today.day,
                PumpName__PumpName=wellName
            ).values("DateCreate","MotorCurrent","HeadPressure","MotorFrequency").order_by('-DateCreate')
        return result

    def search_by_interval_data_all(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_today_data_all(self, interval, wellName):
        Today = date.today()
        result = self.filter(
                DateCreate__year=Today.year,
                DateCreate__month=Today.month,
                DateCreate__day=Today.day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
        return result

    def search_last_data(self, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).last()
        return result

class WellTestManager(models.Manager):
    def search_by_intervals_WellTest(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_by_all_WellTest(self, interval, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
        return result

class SampleTestManager(models.Manager):
    def search_by_intervals_SampleTest(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_by_all_SampleTest(self, interval, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
        return result

class BuildUpTestManager(models.Manager):
    def search_by_intervals_BuilUpTest(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_by_all_BuildUpTest(self, interval, wellName):
        result = self.filter(
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
        return result

class RPDataManager(models.Manager):
    def search_by_interval_RPdata(self, interval, wellName):
        Intervals = interval.split(' to ')
        intervals = [ datetime.strptime(dt,"%Y-%m-%d") for dt in Intervals]
        print(intervals)
        if len(intervals)==1:
            result = self.filter(
                DateCreate__year=intervals[0].year,
                DateCreate__month=intervals[0].month,
                DateCreate__day=intervals[0].day,
                PumpName__PumpName=wellName
            ).values(
                "DateCreate",
                "LoadPump",
                "Position",
                "HeadPressure",
                "PumpFill",
                "CasingPressure",
                "HeadTemperature",
                "PumpFill",
                "SPM",
                "Recomendation"
            ).order_by('-DateCreate')
            return result 
        else:
            result = self.filter(
                DateCreate__range=(intervals[0],intervals[1]),
                PumpName__PumpName=wellName
            ).order_by('-DateCreate')
            return result

    def search_today_RPata(self,wellName):
        Today = date.today()
        result = self.filter(
                DateCreate__year=Today.year,
                DateCreate__month=Today.month,
                DateCreate__day=Today.day,
                PumpName__PumpName=wellName
            ).values(
                "id",
                "DateCreate",
                "LoadPump",
                "Position",
                "HeadPressure",
                "PumpFill",
                "CasingPressure",
                "HeadTemperature",
                "PumpFill",
                "SPM",
                "Recomendation",
                "Diagnosis"
            ).order_by('-DateCreate')
        return result