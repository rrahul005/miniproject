# Generated by Django 2.2.3 on 2020-07-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='storedatamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=500)),
                ('dist', models.CharField(max_length=300)),
                ('yeild', models.CharField(max_length=300)),
                ('year', models.CharField(max_length=300)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
    ]
