# Generated by Django 3.2.7 on 2021-09-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycalendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='english_name',
            field=models.TextField(default='asdas'),
            preserve_default=False,
        ),
    ]