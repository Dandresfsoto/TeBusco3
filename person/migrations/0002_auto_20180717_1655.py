# Generated by Django 2.0.7 on 2018-07-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Nacimiento'),
        ),
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='disappereance',
            field=models.DateField(blank=True, null=True, verbose_name='Desaoarición'),
        ),
    ]