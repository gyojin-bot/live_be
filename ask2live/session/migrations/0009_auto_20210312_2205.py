# Generated by Django 3.1.7 on 2021-03-12 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('session', '0008_auto_20210312_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='host_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.user'),
        ),
    ]
