from django.urls import path
from mail_send.apps import MailSendConfig
from mail_send.views import ServiceClientListView, MailingSetupListView, EmailMessageListView, MailingLogsListView, \
    ServiceClientDetailView, MailingSetupDetailView, EmailMessageDetailView, MailingLogsDetailView, \
    ServiceClientCreateView, ServiceClientUpdateView, ServiceClientDeleteView, MailingSetupCreateView, \
    MailingSetupUpdateView, MailingSetupDeleteView

app_name = MailSendConfig.name


urlpatterns = [
    path('service_client/', ServiceClientListView.as_view(), name='service_client_view'),
    path('service_client/<int:pk>/', ServiceClientDetailView.as_view(), name='service_client_detail'),
    path('service_client/create/', ServiceClientCreateView.as_view(), name='service_client_create'),
    path('service_client/update/<int:pk>/', ServiceClientUpdateView.as_view(), name='service_client_update'),
    path('service_client/delete/<int:pk>/', ServiceClientDeleteView.as_view(), name='service_client_delete'),
    path('mailing_setup/', MailingSetupListView.as_view(), name='mailing_setup_view'),
    path('mailing_setup/<int:pk>/', MailingSetupDetailView.as_view(), name='mailing_setup_detail'),
    path('mailing_setup/create/', MailingSetupCreateView.as_view(), name='mailing_setup_create'),
    path('mailing_setup/update/<int:pk>', MailingSetupUpdateView.as_view(), name='mailing_setup_update'),
    path('mailing_setup/delete/<int:pk>/', MailingSetupDeleteView.as_view(), name='mailing_setup_delete'),
    path('email_message/', EmailMessageListView.as_view(), name='email_message_view'),
    path('email_message/<int:pk>/', EmailMessageDetailView.as_view(), name='email_message_detail'),
    path('mailing_logs/', MailingLogsListView.as_view(), name='mailing_logs_view'),
    path('mailing_logs/<int:pk>/', MailingLogsDetailView.as_view(), name='mailing_logs_detail'),
]
