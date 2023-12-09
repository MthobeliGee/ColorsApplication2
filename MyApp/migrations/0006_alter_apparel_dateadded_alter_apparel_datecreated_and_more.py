# Generated by Django 4.2.3 on 2023-12-09 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_apparel_datecreated_alter_apparel_dateadded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparel',
            name='DateAdded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 1, 17, 5, 345383)),
        ),
        migrations.AlterField(
            model_name='apparel',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 1, 17, 5, 345383)),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 1, 17, 5, 343381)),
        ),
        migrations.AlterField(
            model_name='application',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 1, 17, 5, 343381)),
        ),
        migrations.AlterField(
            model_name='federationpersonel',
            name='PersonelPhone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='federationpersonel',
            name='dateSelected',
            field=models.DateField(default=datetime.datetime(2023, 12, 10, 1, 17, 5, 343381)),
        ),
    ]
