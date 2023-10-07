from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Club(models.Model):

    TIER_CHOICES = (
        ('FREE', 'Free'),
        ('TIER1', 'Members Management - €49'),
        ('TIER2', 'Advanced Features - €99'),
        ('TIER3', 'Complete Access - €120'),

    )
    club_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="club")
    club_name = models.CharField(max_length=255)
    subscription_tier = models.CharField(choices=TIER_CHOICES, default='FREE', max_length=10)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)  

    # Address related fields
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_or_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_feature(self, feature):
        features = {
            'FREE': ['VIEW_MEMBERS', 'ADD_MEMBERS'],
            'TIER1': ['VIEW_MEMBERS', 'ADD_MEMBERS', 'MEMBERS_MANAGEMENT', 'ACCOUNTING'],
            'TIER2': ['VIEW_MEMBERS', 'ADD_MEMBERS', 'MEMBERS_MANAGEMENT', 'ACCOUNTING', 'WEED_INVENTORY', 'BAR_INVENTORY'],
            'TIER3': ['VIEW_MEMBERS', 'ADD_MEMBERS', 'MEMBERS_MANAGEMENT', 'ACCOUNTING', 'WEED_INVENTORY', 'BAR_INVENTORY', 'ANALYTICS', 'AI_PREDICTIONS'],
        }
        return feature in features.get(self.subscription_tier, [])
