# Generated by Django 3.1.3 on 2020-11-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20201112_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='job_date',
            field=models.DateField(),
        ),
    ]
