# Generated by Django 4.1.7 on 2023-06-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_doctor_special_alter_client_region_alter_history_dep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='kabinet',
            field=models.IntegerField(default=0, verbose_name='Кабинет'),
        ),
    ]