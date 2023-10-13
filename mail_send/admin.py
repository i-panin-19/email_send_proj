from django.contrib import admin

from mail_send.models import ServiceClient, MailingSetup, EmailMessage, MailingLogs


@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'full_name', 'comment')


@admin.register(MailingSetup)
class MailingSetupAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'mailing_status')
    list_filter = ('mailing_status',)


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('client', 'letter_subject', 'body_letter')
    list_filter = ('client',)

@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('message', 'last_datetime', 'status', 'log_message')
    list_filter = ('status',)
