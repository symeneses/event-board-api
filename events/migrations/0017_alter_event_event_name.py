# Generated by Django 4.0.3 on 2022-08-25 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_alter_event_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]