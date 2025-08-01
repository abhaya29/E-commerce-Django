# Generated by Django 5.2.4 on 2025-07-22 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_email_customer_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
