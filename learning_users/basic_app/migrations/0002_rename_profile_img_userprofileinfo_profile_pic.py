# Generated by Django 4.2.4 on 2023-10-22 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_img',
            new_name='profile_pic',
        ),
    ]
