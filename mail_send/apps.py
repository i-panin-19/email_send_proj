from django.apps import AppConfig
from mail_send import jobs


class MailSendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_send'

    def ready(self):
        jobs.start()
