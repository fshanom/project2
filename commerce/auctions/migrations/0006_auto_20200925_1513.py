# Generated by Django 3.1.1 on 2020-09-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200924_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
