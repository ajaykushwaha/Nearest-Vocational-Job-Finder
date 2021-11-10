# Generated by Django 3.1.3 on 2020-11-11 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myprofile', '0002_auto_20201111_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_details',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_desc', models.TextField(null=True)),
                ('job_email', models.EmailField(max_length=254, null=True)),
                ('phone_no', models.TextField(max_length=10, null=True)),
                ('job_price', models.IntegerField(null=True)),
                ('job_time', models.TimeField(auto_now=True)),
                ('job_date', models.DateField(auto_now=True)),
                ('job_latitude', models.FloatField(null=True)),
                ('job_address', models.TextField(null=True)),
                ('job_longitude', models.FloatField(null=True)),
                ('job_skill', models.TextField(null=True)),
                ('job_distance', models.IntegerField(null=True)),
                ('is_job_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='applied_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_job_approved', models.BooleanField(default=False)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.job_details')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.profile_details')),
            ],
        ),
    ]