# Generated by Django 4.2.6 on 2023-10-07 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('club_name', models.CharField(max_length=255)),
                ('subscription_tier', models.CharField(choices=[('FREE', 'Free'), ('TIER1', 'Members Management - €49'), ('TIER2', 'Advanced Features - €99'), ('TIER3', 'Complete Access - €120')], default='FREE', max_length=10)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=255, null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state_or_province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='club', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
