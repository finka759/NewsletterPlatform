# Generated by Django 4.2.2 on 2024-07-01 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_mailingparameters_creator_message_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingparameters',
            name='interval',
            field=models.CharField(choices=[('per_day', 'раз в день'), ('per_week', 'раз в неделю'), ('per_month', 'раз в месяц')], default='per_day', max_length=50, verbose_name='интервал рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingparameters',
            name='next_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 10, 54, 58, 624437, tzinfo=datetime.timezone.utc), verbose_name='дата следующей рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingparameters',
            name='status',
            field=models.CharField(choices=[('not_active', 'не_активна'), ('is_active', 'запущена'), ('finished', 'закончена успешно'), ('finished_date', 'закончена по сроку'), ('finished_error', 'законечена с ошибками')], default='not_active', max_length=50, verbose_name='Статус рассылки'),
        ),
    ]