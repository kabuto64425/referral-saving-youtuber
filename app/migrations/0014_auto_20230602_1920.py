# Generated by Django 2.1.2 on 2023-06-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20230602_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='recently_upload_video_tumbnail',
        ),
        migrations.AddField(
            model_name='item',
            name='recently_upload_video_tumbnail_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='recently_upload_video_tumbnail_url'),
        ),
    ]
