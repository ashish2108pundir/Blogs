# Generated by Django 3.0.8 on 2020-08-05 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='title',
        ),
    ]
