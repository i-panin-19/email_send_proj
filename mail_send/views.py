from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail_send.forms import ServiceClientForm, MailingSetupForm
from mail_send.models import ServiceClient, MailingSetup, EmailMessage, MailingLogs


class ServiceClientListView(ListView):
    model = ServiceClient
    extra_context = {
        'title': 'Email-адреса клиентов'
    }


class ServiceClientDetailView(DetailView):
    model = ServiceClient
    extra_context = {
        'title': 'Карточка клиента'
    }


class ServiceClientCreateView(CreateView):
    model = ServiceClient
    form_class = ServiceClientForm
    success_url = reverse_lazy('mail_send:service_client_view')
    extra_context = {
        'title': 'Добавление карточки клиента'
    }


class ServiceClientUpdateView(UpdateView):
    model = ServiceClient
    form_class = ServiceClientForm
    success_url = reverse_lazy()
    extra_context = {
        'title': 'Редактирование карточки клиента'
    }

    def get_success_url(self):
        return reverse('mail_send:service_client_detail', args=[self.object.pk])


class ServiceClientDeleteView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy('mail_send:service_client_view')
    extra_context = {
        'title': 'Удаление карточки клиента'
    }


class MailingSetupListView(ListView):
    model = MailingSetup
    extra_context = {
        'title': 'Рассылки'
    }


class MailingSetupDetailView(DetailView):
    model = MailingSetup
    extra_context = {
        'title': 'Рассылка подробно'
    }


class MailingSetupCreateView(CreateView):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy('mail_send:mailing_setup_view')
    extra_context = {
        'title': 'Создание рассылки'
    }


class MailingSetupUpdateView(UpdateView):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy()
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_success_url(self):
        return reverse('mail_send:mailing_setup_detail', args=[self.object.pk])


class MailingSetupDeleteView(DeleteView):
    model = MailingSetup
    success_url = reverse_lazy('mail_send:mailing_setup_view')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class EmailMessageListView(ListView):
    model = EmailMessage
    extra_context = {
        'title': 'Сообщения'
    }


class EmailMessageDetailView(DetailView):
    model = EmailMessage
    extra_context = {
        'title': 'Сообщение подробно'
    }


class MailingLogsListView(ListView):
    model = MailingLogs
    extra_context = {
        'title': 'Логи'
    }


class MailingLogsDetailView(DetailView):
    model = MailingLogs
    extra_context = {
        'title': 'Логи подробно'
    }
