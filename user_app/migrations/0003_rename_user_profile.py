# Generated by Django 5.0.7 on 2024-07-13 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_user_email_user_phone_alter_user_birthday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
