# Generated by Django 4.0.3 on 2022-07-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_accessibility_options_event_event_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]