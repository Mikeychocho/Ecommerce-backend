# Generated by Django 4.1.1 on 2022-11-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='wishlist',
            field=models.BooleanField(default=False),
        ),
    ]
