# Generated by Django 5.1.4 on 2024-12-17 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=18)),
                ('currency', models.CharField(choices=[('USD', 'Dólar Americano'), ('BRL', 'Real'), ('PYG', 'Guaraní'), ('ARS', 'Peso Argentino'), ('EUR', 'Euro')], max_length=100)),
                ('institution', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(choices=[(False, 'Inactive'), (True, 'Active')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.accounttype')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
