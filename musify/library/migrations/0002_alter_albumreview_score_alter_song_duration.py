# Generated by Django 4.1.7 on 2023-03-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='score',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
