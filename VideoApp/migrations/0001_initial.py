# Generated by Django 3.1 on 2020-09-08 10:54

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
            name='UploadVideoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_capition', models.CharField(max_length=500)),
                ('video_file', models.FileField(upload_to='uploaded_videos')),
                ('video_url', models.CharField(max_length=1000)),
                ('video_tags', models.CharField(max_length=2000)),
                ('video_likes', models.IntegerField()),
                ('root_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]