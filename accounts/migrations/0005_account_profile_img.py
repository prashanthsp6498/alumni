# Generated by Django 2.2.7 on 2019-11-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alumniprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_img',
            field=models.ImageField(default='profile_image/default_img.png', upload_to='profile_image/'),
        ),
    ]
