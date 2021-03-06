# Generated by Django 2.2.2 on 2021-02-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('appointment_start_time', models.TimeField()),
                ('appointment_end_time', models.TimeField()),
            ],
        ),
    ]
