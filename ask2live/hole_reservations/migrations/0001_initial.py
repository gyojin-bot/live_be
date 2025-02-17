# Generated by Django 3.1.7 on 2021-03-14 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('holes', '0002_auto_20210314_2228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=12)),
                ('target_demand', models.IntegerField(blank=True, null=True)),
                ('reserve_start_date', models.DateTimeField(blank=True, null=True)),
                ('finish_date', models.DateTimeField(blank=True, null=True)),
                ('guests', models.ManyToManyField(blank=True, related_name='hole_reservations', to=settings.AUTH_USER_MODEL)),
                ('hole', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='hole_reservations', to='holes.hole')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
