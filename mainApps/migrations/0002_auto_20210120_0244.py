# Generated by Django 3.1.2 on 2021-01-19 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='favoriteKitchen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainApps.kitchen'),
        ),
    ]
