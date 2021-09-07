# Generated by Django 3.2.6 on 2021-09-04 19:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0011_alter_purchase_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 12, 51, 7, 522547)),
        ),
    ]