# Generated by Django 3.0.8 on 2020-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild_bank', '0002_auto_20200731_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
