from django.db import models
from django.utils import timezone

from client.models import Client

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name='тема письма', **NULLABLE)
    content = models.TextField(verbose_name='содержимое письма')

    def __str__(self):
        return f'{self.theme} {self.content}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class MailingParameters(models.Model):
    intervals = (
        ('once', 'разово'),
        ('per_day', 'раз в день'),
        ('per_week', 'раз в неделю'),
        ('per_month', 'раз в месяц')
    )
    status_variants = (
        ('created', 'создана'),
        ('executing', 'запущена'),
        ('finished', 'закончена успешно'),
        ('error', 'законечена с ошибками')
    )
    name = models.CharField(verbose_name="название рассылки", max_length=50, default='mailing_no_name')
    client = models.ManyToManyField(Client, verbose_name='получатель')
    mail = models.ForeignKey(Message, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now, verbose_name='начало рассылки')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='конец рассылки')
    next_date = models.DateTimeField(default=timezone.now, verbose_name='дата следующей рассылки')
    is_active = models.BooleanField(default=True, verbose_name="активна")
    interval = models.CharField(default='once', max_length=50, choices=intervals, verbose_name="интервал рассылки")
    status = models.CharField(max_length=15, choices=status_variants, default='created', verbose_name='Статус рассылки')

    def __str__(self):
        return f'{self.name}: ({self.start_time} - {self.end_time};интервал:{self.interval}; активность:{self.is_active})'

    class Meta:
        verbose_name = 'настройка рассылкм'
        verbose_name_plural = 'настройки рассылок'
        permissions = [
            (
                'toggle_active',
                'выключить рассылку'
            ),
        ]


class Logs(models.Model):
    mailing_parameters = models.ForeignKey(MailingParameters, on_delete=models.CASCADE,
                                           verbose_name='параметры_рассылки')
    last_time_sending = models.DateTimeField(auto_now=True, verbose_name='время последней рассылки', **NULLABLE)
    status = models.CharField(max_length=50, verbose_name='статус попытки', **NULLABLE)
    response = models.CharField(max_length=200, verbose_name="ответ почтового сервера", **NULLABLE)


    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

    def __str__(self):
        return f'''Отправлено: {self.last_time_sending},
               f'Статус: {self.status}'''
