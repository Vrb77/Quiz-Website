# Generated by Django 3.1.4 on 2021-10-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_c3model_c4model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c1model',
            name='ans',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='c1model',
            name='op1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='c1model',
            name='op2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='c1model',
            name='op3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='c1model',
            name='op4',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='c1model',
            name='que',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
