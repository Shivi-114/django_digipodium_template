# Generated by Django 3.2 on 2021-06-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210606_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='human_resource',
            name='img',
            field=models.ImageField(default='default_hr.jpg', upload_to='hr/'),
        ),
    ]
