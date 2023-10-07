from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.club_dashboard, name='club_dashboard'),
]