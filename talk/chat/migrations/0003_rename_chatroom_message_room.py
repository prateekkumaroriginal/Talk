# Generated by Django 5.0 on 2023-12-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chatroom',
            new_name='room',
        ),
    ]