# Generated by Django 3.2.4 on 2021-06-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0004_auto_20210616_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_id',
            field=models.IntegerField(default=0),
        ),
    ]
