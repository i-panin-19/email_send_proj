from django import forms

from mail_send.models import ServiceClient, MailingSetup, EmailMessage


class ServiceClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = '__all__'


class MailingSetupForm(forms.ModelForm):
    class Meta:
        model = MailingSetup
        fields = '__all__'


class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = '__all__'
