# Generated by Django 4.2.1 on 2024-12-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
