# Generated by Django 2.1.8 on 2019-06-01 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relacion',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='relacion',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]