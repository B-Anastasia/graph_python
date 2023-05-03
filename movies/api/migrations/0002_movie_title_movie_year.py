# Generated by Django 4.2.1 on 2023-05-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=2000),
        ),
    ]
