# Generated by Django 3.2.7 on 2021-09-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycalendar', '0002_category_english_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='english_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categorytitle',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
