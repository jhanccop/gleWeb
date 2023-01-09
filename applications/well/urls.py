from django.urls import path
from . import views

urlpatterns = [
    path('overview/<company>', views.ListWellsCompany.as_view()),
]
