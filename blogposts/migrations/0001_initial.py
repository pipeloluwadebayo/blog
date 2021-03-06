# Generated by Django 3.2.7 on 2021-10-29 15:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
                ('github_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_tag', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('snippet', models.CharField(default='Read More...', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('body', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogposts.post')),
            ],
        ),
    ]
