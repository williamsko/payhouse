# Generated by Django 2.2.4 on 2019-09-07 16:58

from django.db import migrations, models
import partner.models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='reference',
            field=models.CharField(default=partner.models.Partner.reference, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='partnerbalance',
            name='reference',
            field=models.CharField(default=partner.models.PartnerBalance.reference, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='reference',
            field=models.CharField(default=partner.models.Service.reference, max_length=255, unique=True),
        ),
    ]
