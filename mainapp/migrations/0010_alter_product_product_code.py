# Generated by Django 4.0.4 on 2022-06-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(blank=True, default=263065, verbose_name='Код продукту'),
        ),
    ]