# Generated by Django 4.2 on 2023-05-18 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_product_stock'),
        ('customer', '0006_customer_adtype_customer_lname_customer_locality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='farmid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farmer.registeration'),
        ),
    ]
