# Generated by Django 2.1.5 on 2019-01-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilogram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumname_image',
        ),
        migrations.AddField(
            model_name='photo',
            name='thumnail_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
