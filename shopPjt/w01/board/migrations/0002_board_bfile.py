# Generated by Django 5.1.3 on 2024-12-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='bfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
