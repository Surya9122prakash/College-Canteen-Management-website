# Generated by Django 4.0.6 on 2022-08-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0009_rename_orderstat_order_order_confirmed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='sno',
            field=models.IntegerField(default=1),
        ),
    ]