# Generated by Django 3.1.7 on 2021-03-14 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='livehole',
            name='hole',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='liveholes', to='holes.hole'),
        ),
        migrations.AddField(
            model_name='livehole',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='liveholes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hole',
            name='host',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='hole', to=settings.AUTH_USER_MODEL),
        ),
    ]
