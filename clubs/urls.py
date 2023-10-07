from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Keep this line as well
    path('', views.club_dashboard, name='club_dashboard'),
    path('dashboard/', views.club_dashboard, name='club_dashboard'),
]
