# Generated by Django 4.0.4 on 2022-05-14 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_productservice_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductService',
            new_name='ProductActivity',
        ),
        migrations.RenameModel(
            old_name='SaleProductService',
            new_name='SaleProductActivity',
        ),
        migrations.AlterModelOptions(
            name='productactivity',
            options={'verbose_name': 'ProductActivity', 'verbose_name_plural': 'ProductActivitys'},
        ),
        migrations.AlterModelOptions(
            name='saleproductactivity',
            options={'verbose_name': 'SaleProductActivity', 'verbose_name_plural': 'SaleProductActivitys'},
        ),
        migrations.RenameField(
            model_name='saleproductactivity',
            old_name='product_service',
            new_name='product_activity',
        ),
    ]
