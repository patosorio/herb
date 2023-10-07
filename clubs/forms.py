from allauth.account.forms import SignupForm
from django import forms
from .models import Club

class CustomSignUpForm(SignupForm):
    club_name = forms.CharField(max_length=255, required=True, label='Club Name')
    street_address = forms.CharField(max_length=255, required=True, label='Street Address')
    city = forms.CharField(max_length=100, required=True, label='City')
    state_or_province = forms.CharField(max_length=100, required=True, label='State/Province')
    postal_code = forms.CharField(max_length=10, required=True, label='Postal Code')
    country = forms.CharField(max_length=100, required=True, label='Country')
    subscription_tier = forms.ChoiceField(choices=Club.TIER_CHOICES, initial='FREE', required=True, label='Subscription Tier')

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        club = Club.objects.create(
            owner=user,
            club_name=self.cleaned_data.get('club_name'),
            street_address=self.cleaned_data.get('street_address'),
            city=self.cleaned_data.get('city'),
            state_or_province=self.cleaned_data.get('state_or_province'),
            postal_code=self.cleaned_data.get('postal_code'),
            country=self.cleaned_data.get('country'),
            subscription_tier=self.cleaned_data.get('subscription_tier')
        )
        return user
