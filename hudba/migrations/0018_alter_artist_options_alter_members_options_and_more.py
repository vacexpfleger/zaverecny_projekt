# Generated by Django 4.0.4 on 2022-12-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0017_alter_members_options_artist_image_delete_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={},
        ),
        migrations.AlterField(
            model_name='artist',
            name='about',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to='artists/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudba.origin'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='year_begin',
            field=models.DateField(),
        ),
    ]