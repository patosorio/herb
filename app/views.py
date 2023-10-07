from django.shortcuts import redirect
from django.urls import reverse

def home_redirect(request):
    if request.user.is_authenticated:
        print("User is authenticated, redirecting to dashboard")
        return redirect(reverse('club_dashboard'))
    else:
        print("User is not authenticated, redirecting to login page")
        return redirect(reverse('account_login'))
