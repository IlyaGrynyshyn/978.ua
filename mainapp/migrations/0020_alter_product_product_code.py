# Generated by Django 4.0.4 on 2022-06-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(blank=True, default=470025, verbose_name='Код продукту'),
        ),
    ]
