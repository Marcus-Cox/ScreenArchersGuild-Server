# Generated by Django 4.1.4 on 2022-12-13 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenarchersguildapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screenshot',
            old_name='isMooded',
            new_name='isModded',
        ),
    ]