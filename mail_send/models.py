from django.db import models


NULLABLE = {'blank': True, 'null': True}


class ServiceClient(models.Model):
    email = models.EmailField(max_length=254, verbose_name='email')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}   {self.full_name}   ({self.comment})'

    class Meta:
        verbose_name = 'почта клиента'
        verbose_name_plural = 'адреса клиентов'


class MailingSetup(models.Model):
    periodicity_list = [
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц')
    ]
    mailing_status_list = [
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена')
    ]

    mailing_time = models.TimeField(auto_now=True, auto_now_add=False, verbose_name='время рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=20, choices=periodicity_list, verbose_name='периодичность', default='day')
    mailing_status = models.CharField(max_length=20, choices=mailing_status_list, verbose_name='статус рассылки', default='completed')

    def __str__(self):
        return f'{self.mailing_time}   {self.periodicity} -> ({self.mailing_status})'

    class Meta:
        verbose_name = 'настройки рассылки'
        verbose_name_plural = 'настроек рассылки'
