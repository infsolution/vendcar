# Generated by Django 2.1.4 on 2018-12-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20181209_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='acessorio',
            field=models.ManyToManyField(blank=True, to='store.Acessorio'),
        ),
    ]