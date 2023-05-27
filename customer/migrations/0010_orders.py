# Generated by Django 4.2 on 2023-05-22 09:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_cart_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=20)),
                ('adtype', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=15)),
                ('zipcode', models.CharField(max_length=10)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('paystatus', models.BooleanField(default=False)),
                ('approval', models.BooleanField(default=False)),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.cart')),
                ('cusid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]