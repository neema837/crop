# Generated by Django 4.2 on 2023-05-04 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categ', models.CharField(max_length=20)),
                ('bdes', models.CharField(max_length=50)),
                ('bimage', models.FileField(upload_to='users')),
                ('farmid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.registeration')),
            ],
        ),
    ]
