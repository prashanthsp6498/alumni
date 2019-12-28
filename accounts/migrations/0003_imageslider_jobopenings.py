# Generated by Django 2.2.7 on 2019-11-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191126_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='slider/')),
            ],
        ),
        migrations.CreateModel(
            name='JobOpenings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('salary', models.IntegerField(null=True)),
                ('company', models.CharField(max_length=200)),
                ('hr_email', models.CharField(max_length=50)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
