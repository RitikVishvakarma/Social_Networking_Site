# Generated by Django 3.1.5 on 2021-02-04 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='uesr',
            new_name='user',
        ),
    ]
