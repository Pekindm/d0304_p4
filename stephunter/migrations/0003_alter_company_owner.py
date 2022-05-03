# Generated by Django 4.0.4 on 2022-04-27 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stephunter', '0002_company_owner_alter_company_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
