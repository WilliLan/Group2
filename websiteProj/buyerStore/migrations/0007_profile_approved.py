# Generated by Django 5.1.2 on 2024-11-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyerStore', '0006_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
