# Generated by Django 3.2.7 on 2021-11-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
