# Generated by Django 4.2 on 2023-04-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_clientmodel_owner_clientmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='city',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='institution',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='nin',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='type_of_institution',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
