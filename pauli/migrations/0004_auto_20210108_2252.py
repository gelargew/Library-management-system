# Generated by Django 3.1.4 on 2021-01-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pauli', '0003_auto_20210106_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timeleft',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='result',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
