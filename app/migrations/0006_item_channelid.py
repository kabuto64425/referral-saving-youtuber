# Generated by Django 2.1.2 on 2023-05-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_item_subscriber_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='channelId',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='channelId'),
        ),
    ]