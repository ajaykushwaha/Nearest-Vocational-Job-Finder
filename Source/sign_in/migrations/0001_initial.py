# Generated by Django 3.1.3 on 2020-11-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contest', models.TextField(blank=True, null=True)),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
    ]
