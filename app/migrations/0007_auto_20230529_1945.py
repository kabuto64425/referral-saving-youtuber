# Generated by Django 2.1.2 on 2023-05-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_item_channelid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='subscriber_count',
        ),
        migrations.AddField(
            model_name='item',
            name='video_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='video_count'),
        ),
    ]
