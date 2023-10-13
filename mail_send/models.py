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

    mailing_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=20, choices=periodicity_list, verbose_name='периодичность', default='day')
    mailing_status = models.CharField(max_length=20, choices=mailing_status_list, verbose_name='статус рассылки', default='completed')

    def __str__(self):
        return f'{self.mailing_time}   {self.periodicity} -> ({self.mailing_status})'

    class Meta:
        verbose_name = 'настройки рассылки'
        verbose_name_plural = 'настроек рассылки'


class EmailMessage(models.Model):
    client = models.ForeignKey('ServiceClient', on_delete=models.PROTECT, **NULLABLE, verbose_name='клиент')
    letter_subject = models.CharField(max_length=200, verbose_name='тема письма')
    body_letter = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.client}   {self.letter_subject}'

    class Meta:
        verbose_name = 'сообщение рассылки'
        verbose_name_plural = 'сообщений рассылки'


class MailingLogs(models.Model):
    message = models.ForeignKey('EmailMessage', on_delete=models.PROTECT, **NULLABLE, verbose_name='письмо')
    last_datetime = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='дата попытки', **NULLABLE)
    status = models.BooleanField(verbose_name='статус попытки')
    log_message = models.TextField(verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return f'{self.message}   status: {self.status}   {self.last_datetime} -> {self.log_message}'

    class Meta:
        verbose_name = 'логи рассылки'
        verbose_name_plural = 'логи рассылок'
