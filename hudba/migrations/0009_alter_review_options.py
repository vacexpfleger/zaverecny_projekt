# Generated by Django 4.0.4 on 2022-05-26 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0008_alter_review_options_alter_track_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-rating', 'reviewer']},
        ),
    ]
