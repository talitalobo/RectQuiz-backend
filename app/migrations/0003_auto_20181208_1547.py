# Generated by Django 2.1.4 on 2018-12-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181207_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='explicacao',
            field=models.TextField(null=True, verbose_name='Explicação'),
        ),
    ]
