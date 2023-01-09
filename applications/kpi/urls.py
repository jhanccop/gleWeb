from django.urls import path
from . import views

app_name = "kpi_app"

urlpatterns = [
    path('kpi/deferment', views.ListFieldDeferment.as_view(),name = "deferment"),
    path('kpi/run-life', views.ListFieldRunLife.as_view(),name = "run-life"),
    path('kpi/failure-rate', views.ListFieldFailureRate.as_view(),name = "failure-rate"),
]