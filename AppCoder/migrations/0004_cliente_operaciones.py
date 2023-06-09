# Generated by Django 4.1.7 on 2023-04-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ape', models.CharField(max_length=40)),
                ('cuil_t', models.IntegerField()),
                ('sit_fis', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=40)),
                ('sucursal', models.CharField(max_length=40)),
                ('cbu', models.IntegerField()),
            ],
        ),
    ]
