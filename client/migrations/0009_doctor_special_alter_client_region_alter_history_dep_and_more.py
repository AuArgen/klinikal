# Generated by Django 4.1.7 on 2023-06-07 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_diognoz_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='special',
            field=models.CharField(default='Врач', max_length=255, verbose_name='Специалист'),
        ),
        migrations.AlterField(
            model_name='client',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='history',
            name='dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.departament', verbose_name='Отделения'),
        ),
        migrations.AlterField(
            model_name='history',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='history',
            name='diognoz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.diognoz', verbose_name='Диогноз'),
        ),
        migrations.AlterField(
            model_name='history',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.doctor', verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='history',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='history',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.region', verbose_name='Регион'),
        ),
    ]
