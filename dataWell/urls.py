from django.urls import path
from . import views

urlpatterns = [
    path('rod-pump/<PumpName>', views.ListRodPump.as_view()),
    path('es-pump/<PumpName>', views.ListESPump.as_view()),
]
