# Generated by Django 3.1.4 on 2021-10-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_auto_20211008_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='c3Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=300)),
                ('op1', models.CharField(max_length=300)),
                ('op2', models.CharField(max_length=300)),
                ('op3', models.CharField(max_length=300)),
                ('op4', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='c4Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=300)),
                ('op1', models.CharField(max_length=300)),
                ('op2', models.CharField(max_length=300)),
                ('op3', models.CharField(max_length=300)),
                ('op4', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=300)),
            ],
        ),
    ]
