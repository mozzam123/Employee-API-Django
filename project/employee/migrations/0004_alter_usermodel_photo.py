# Generated by Django 4.2.7 on 2023-11-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_usermodel_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.TextField(blank=True),
        ),
    ]