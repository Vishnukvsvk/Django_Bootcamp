# Generated by Django 3.1.2 on 2020-11-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=True),
        ),
    ]
