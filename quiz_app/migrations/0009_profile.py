# Generated by Django 3.1.4 on 2021-10-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0008_auto_20211017_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('mail', models.CharField(max_length=300)),
            ],
        ),
    ]
