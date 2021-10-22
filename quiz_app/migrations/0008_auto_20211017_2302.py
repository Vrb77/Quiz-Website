# Generated by Django 3.1.4 on 2021-10-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_auto_20211016_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('mail', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=500)),
                ('msg', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='history',
        ),
    ]
