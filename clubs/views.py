from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Club

# Create your views here.

def club_dashboard(request):
    if request.user.is_authenticated:
        try:
            club = Club.objects.get(owner=request.user)

            context = {
                'club' : club,
            }

            return render(request, 'clubs/dashboard.html', context)
        except Club.DoesNotExist:
            return redirect(reverse('account_login'))

    else:
        return redirect(reverse('account_login'))
