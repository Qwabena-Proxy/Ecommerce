# Generated by Django 4.1.10 on 2023-10-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_machinebrand_machinecategory_machine_is_sale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machinePrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
