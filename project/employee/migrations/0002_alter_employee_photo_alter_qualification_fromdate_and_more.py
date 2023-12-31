# Generated by Django 4.2.7 on 2023-11-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='fromDate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='toDate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='fromDate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='toDate',
            field=models.CharField(max_length=255),
        ),
    ]
