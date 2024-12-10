# Generated by Django 5.1.3 on 2024-12-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ano', models.IntegerField(unique=True)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('tel', models.CharField(default='010-0000-0000', max_length=20)),
                ('role', models.IntegerField()),
                ('adate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
