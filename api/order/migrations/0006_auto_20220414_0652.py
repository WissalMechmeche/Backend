# Generated by Django 3.0.8 on 2022-04-14 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220412_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer_Or',
        ),
    ]
