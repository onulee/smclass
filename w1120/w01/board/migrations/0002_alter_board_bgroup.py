# Generated by Django 5.1.3 on 2024-11-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bgroup',
            field=models.IntegerField(blank=True),
        ),
    ]
