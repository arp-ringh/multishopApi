# Generated by Django 4.1.3 on 2022-11-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_orderitem_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="customer",
        ),
    ]
