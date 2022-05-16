# Generated by Django 4.0.4 on 2022-05-15 02:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_alter_productactivity_commission_alter_sale_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productactivity',
            name='commission',
            field=models.IntegerField(default=0, error_messages={'invalid_error': 'A comissão deve estar entre 0 e 10'}, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]