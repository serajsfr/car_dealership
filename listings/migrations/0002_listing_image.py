# Generated by Django 5.0.7 on 2024-07-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default=' ', upload_to=''),
            preserve_default=False,
        ),
    ]
