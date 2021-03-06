# Generated by Django 2.1.4 on 2018-12-10 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_auto_20181209_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0)),
                ('concluida', models.BooleanField(default=False)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('prazo_pagamento', models.DateField(blank=True, null=True)),
                ('pagamento_ok', models.BooleanField(default=False)),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carro', to='store.Carro')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comprador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
