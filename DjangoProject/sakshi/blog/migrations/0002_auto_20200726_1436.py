# Generated by Django 3.0.8 on 2020-07-26 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]