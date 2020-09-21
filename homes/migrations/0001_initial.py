# Generated by Django 3.1 on 2020-09-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('Details', models.URLField(max_length=500)),
                ('Buy', models.URLField(max_length=500)),
                ('Types', models.CharField(max_length=50)),
                ('Video', models.URLField(max_length=500)),
            ],
        ),
    ]
