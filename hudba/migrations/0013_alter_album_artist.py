# Generated by Django 4.0.4 on 2022-11-10 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0012_alter_album_about_alter_album_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hudba.artist'),
        ),
    ]
