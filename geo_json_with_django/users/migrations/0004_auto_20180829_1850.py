# Generated by Django 2.1 on 2018-08-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180829_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Full Name'),
        ),
    ]
