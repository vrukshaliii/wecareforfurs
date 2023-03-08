from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.predDisease, name="show")
]
