# Generated by Django 2.1.2 on 2023-06-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20230602_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='recently_upload_video_published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='recently_upload_video_published_at'),
        ),
    ]