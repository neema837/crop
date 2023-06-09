# Generated by Django 4.2 on 2023-05-04 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('cimage', models.FileField(upload_to='users')),
                ('farmid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.registeration')),
            ],
        ),
    ]
