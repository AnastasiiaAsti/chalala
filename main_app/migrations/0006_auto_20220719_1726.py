# Generated by Django 2.2.12 on 2022-07-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
