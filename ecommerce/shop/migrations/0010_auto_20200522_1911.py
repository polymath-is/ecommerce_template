# Generated by Django 3.0.4 on 2020-05-22 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200522_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.PromotionalCode'),
        ),
        migrations.AlterField(
            model_name='promotionalcode',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]
