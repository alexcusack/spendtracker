# Generated by Django 2.1.1 on 2018-09-15 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spendTrackerApp', '0003_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge',
            name='time_of_charge',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge',
            name='vendor',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
