# Generated by Django 2.2.2 on 2021-02-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.CharField(max_length=20, verbose_name='Birth Date'),
        ),
    ]
