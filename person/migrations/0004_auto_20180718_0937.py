# Generated by Django 2.0.7 on 2018-07-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20180718_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personimage',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=2, upload_to='photo'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PersonImage',
        ),
    ]
