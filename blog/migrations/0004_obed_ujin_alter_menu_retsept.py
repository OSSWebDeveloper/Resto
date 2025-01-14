# Generated by Django 4.2.1 on 2023-08-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ovqat nomi')),
                ('rasm', models.ImageField(upload_to='images', verbose_name='Ovqat rasmi')),
                ('retsept', models.TextField(verbose_name='Ovqat haqida')),
                ('narxi', models.IntegerField(default=0, null='True', verbose_name='Narxi')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menular',
            },
        ),
        migrations.CreateModel(
            name='Ujin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ovqat nomi')),
                ('rasm', models.ImageField(upload_to='images', verbose_name='Ovqat rasmi')),
                ('retsept', models.TextField(verbose_name='Ovqat haqida')),
                ('narxi', models.IntegerField(default=0, null='True', verbose_name='Narxi')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menular',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='retsept',
            field=models.TextField(verbose_name='Ovqat haqida'),
        ),
    ]
