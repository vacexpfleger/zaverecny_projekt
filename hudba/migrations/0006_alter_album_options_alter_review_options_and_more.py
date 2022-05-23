# Generated by Django 4.0.4 on 2022-05-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0005_album_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-rating']},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['-number']},
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='albums/'),
        ),
    ]