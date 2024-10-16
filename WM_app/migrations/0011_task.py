# Generated by Django 5.0.4 on 2024-09-24 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WM_app', '0010_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pickup_id', models.CharField(max_length=20)),
                ('status', models.CharField(default='Assigned', max_length=20)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WM_app.staff')),
            ],
        ),
    ]
