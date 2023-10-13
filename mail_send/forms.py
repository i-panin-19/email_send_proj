from django import forms

from mail_send.models import ServiceClient, MailingSetup


class ServiceClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = '__all__'


class MailingSetupForm(forms.ModelForm):
    class Meta:
        model = MailingSetup
        fields = '__all__'
