# Generated by Django 3.1.2 on 2020-10-06 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201006_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritefeatures',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favourite_features', to='api.userprofile'),
        ),
    ]
