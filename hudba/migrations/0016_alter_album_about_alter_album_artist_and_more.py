# Generated by Django 4.0.4 on 2022-11-13 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0015_alter_album_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudba.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='albums/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='hudba.genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudba.label'),
        ),
        migrations.AlterField(
            model_name='album',
            name='length',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.ManyToManyField(to='hudba.genre'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='labels',
            field=models.ManyToManyField(to='hudba.label'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='members',
            field=models.ManyToManyField(to='hudba.members'),
        ),
    ]
