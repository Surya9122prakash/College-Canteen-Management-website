# Generated by Django 4.0.6 on 2022-08-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=50, null=True)),
                ('i_id', models.CharField(max_length=35, null=True)),
                ('price', models.CharField(max_length=35, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='files/thumbnail')),
            ],
        ),
    ]