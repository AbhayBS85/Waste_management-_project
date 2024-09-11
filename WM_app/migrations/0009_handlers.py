# Generated by Django 5.0.4 on 2024-09-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WM_app', '0008_pickup_pickup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handlers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(error_messages={'unique': 'A person with this phone number already exists.'}, max_length=15, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'A person with this email already exists.'}, max_length=254, unique=True)),
            ],
        ),
    ]
