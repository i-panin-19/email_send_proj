# Generated by Django 4.2.5 on 2023-09-25 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail_send', '0003_emailmessage_mailinglogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mail_send.serviceclient', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='mailinglogs',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mail_send.emailmessage', verbose_name='письмо'),
        ),
    ]
