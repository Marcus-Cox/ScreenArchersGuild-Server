# Generated by Django 4.1.4 on 2022-12-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenarchersguildapi', '0003_alter_guide_publishing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='publishing_date',
            field=models.DateField(),
        ),
    ]