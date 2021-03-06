# Generated by Django 3.1.1 on 2020-09-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('job_area', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Worker_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('job_area', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=400)),
            ],
        ),
    ]
