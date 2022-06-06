# Generated by Django 4.0.4 on 2022-06-02 18:10

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name=mainapp.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='img',
            field=models.ImageField(upload_to='images/<function ProductImage.product_name at 0x7f6d511ffa60>'),
        ),
    ]
