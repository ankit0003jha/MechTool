# Generated by Django 3.1 on 2020-09-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_measuringtool1_powertool1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automotivetool1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('Details', models.URLField(max_length=500)),
                ('Buy', models.URLField(max_length=500)),
                ('Video', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Machinetool1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('Details', models.URLField(max_length=500)),
                ('Buy', models.URLField(max_length=500)),
                ('Video', models.URLField(max_length=500)),
            ],
        ),
    ]
