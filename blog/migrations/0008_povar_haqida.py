# Generated by Django 4.2 on 2023-08-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_povar_twitter_alter_povar_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='povar',
            name='haqida',
            field=models.CharField(max_length=255, null=True, verbose_name='Povar haqida'),
        ),
    ]
