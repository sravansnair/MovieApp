# Generated by Django 4.1.3 on 2022-12-09 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]
