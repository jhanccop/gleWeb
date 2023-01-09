from django.urls import path
from . import views

app_name = "overview_app"

urlpatterns = [
    path('overview', views.ListOverview.as_view(),name = "overview"),
    path('overview/electrical-submersible-pump/operation/<PumpName>', views.ListOperationDataESPump.as_view()),
    path('overview/electrical-submersible-pump/trends/<PumpName>', views.ListTrendsDataESPump.as_view()),
    path('overview/electrical-submersible-pump/troubleshoot/<PumpName>', views.ListTroubleshootDataESPump.as_view()),
    path('overview/electrical-submersible-pump/optimization/<PumpName>', views.ListOptimizationDataESPump.as_view()),
    path('overview/electrical-submersible-pump/test/<PumpName>', views.ListTestDataESPump.as_view(), name='create_test'),
    path('overview/electrical-submersible-pump/inputs/<PumpName>', views.ListInputDataESPump.as_view()),
    path('overview/socker-rod-pump/<PumpName>', views.ListDataRodPump.as_view()),
    path('smart_alarms', views.ListSmartAlarms.as_view(),name = "smart_alarms"),
    path('create-well-test/<PumpName>', views.CreateWellTestForm.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
]
