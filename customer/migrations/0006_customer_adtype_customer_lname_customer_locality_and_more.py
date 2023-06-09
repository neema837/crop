# Generated by Django 4.2 on 2023-05-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_cart_created_at_cart_paystatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='adtype',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='locality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
