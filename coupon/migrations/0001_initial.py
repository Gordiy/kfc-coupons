# Generated by Django 3.2.19 on 2023-06-24 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(unique=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.guest')),
            ],
        ),
    ]
