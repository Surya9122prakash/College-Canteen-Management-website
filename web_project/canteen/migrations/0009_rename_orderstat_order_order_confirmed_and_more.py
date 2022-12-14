# Generated by Django 4.0.6 on 2022-08-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0008_alter_menus_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderstat',
            new_name='order_confirmed',
        ),
        migrations.RemoveField(
            model_name='menus',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
