# Generated by Django 4.1.10 on 2023-11-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_gender_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='customerMessage',
            field=models.TextField(),
        ),
    ]
