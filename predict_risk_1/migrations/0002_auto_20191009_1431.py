# Generated by Django 2.2.5 on 2019-10-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions_1',
            name='sg',
            field=models.FloatField(choices=[(1.01, '1.01'), (1.02, '1.02'), (1.015, '1.015'), (1.025, '1.025')], default=1.01),
        ),
    ]
