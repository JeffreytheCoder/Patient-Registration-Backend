# Generated by Django 2.2.2 on 2021-02-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20210210_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]