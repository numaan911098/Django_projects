from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('<int:month>/', views.monthlychallengesbynum),
    path('<str:month>/', views.monthlychallenges, name='month-challenge'),
]