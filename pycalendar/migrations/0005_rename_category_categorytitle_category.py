# Generated by Django 3.2.7 on 2021-09-26 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pycalendar', '0004_category_hex_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorytitle',
            old_name='Category',
            new_name='category',
        ),
    ]