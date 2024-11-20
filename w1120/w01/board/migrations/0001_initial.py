# Generated by Django 5.1.3 on 2024-11-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('bno', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=100)),
                ('btitle', models.CharField(max_length=1000)),
                ('bcontent', models.TextField()),
                ('bgroup', models.IntegerField()),
                ('bstep', models.IntegerField(default=0)),
                ('bindent', models.IntegerField(default=0)),
                ('bhit', models.IntegerField(default=0)),
                ('bdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
