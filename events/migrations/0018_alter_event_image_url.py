# Generated by Django 4.0.3 on 2022-08-25 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_event_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
