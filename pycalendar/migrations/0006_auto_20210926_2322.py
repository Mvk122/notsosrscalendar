# Generated by Django 3.2.7 on 2021-09-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycalendar', '0005_rename_category_categorytitle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='english_description_markdown',
            field=models.TextField(default='asdad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='english_title',
            field=models.TextField(default='asasss'),
            preserve_default=False,
        ),
    ]