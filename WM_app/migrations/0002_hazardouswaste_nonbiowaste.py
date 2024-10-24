# Generated by Django 5.0.4 on 2024-08-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WM_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HazardousWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('weight_option', models.CharField(choices=[('manual', 'Enter manually'), ('later', 'Check later on pick up')], max_length=50)),
                ('manual_weight', models.FloatField(blank=True, null=True)),
                ('location_option', models.CharField(choices=[('manual', 'Enter manually'), ('gps', 'Choose on map')], max_length=50)),
                ('manual_address', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NonBioWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('weight_option', models.CharField(choices=[('manual', 'Enter manually'), ('later', 'Check later on pick up')], max_length=50)),
                ('manual_weight', models.FloatField(blank=True, null=True)),
                ('location_option', models.CharField(choices=[('manual', 'Enter manually'), ('gps', 'Choose on map')], max_length=50)),
                ('manual_address', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
