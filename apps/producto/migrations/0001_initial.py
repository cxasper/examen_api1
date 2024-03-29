# Generated by Django 2.1.8 on 2019-06-01 00:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credito', '0001_initial'),
        ('plazo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_credito', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('numero_cuotas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('saldo', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('plazo_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plazo.Plazo')),
                ('tipo_credito_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='credito.Credito')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
