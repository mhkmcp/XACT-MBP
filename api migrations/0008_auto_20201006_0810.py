# Generated by Django 3.1.2 on 2020-10-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201006_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='demography',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='taxonomy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]