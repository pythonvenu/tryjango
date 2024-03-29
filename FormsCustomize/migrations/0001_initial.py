# Generated by Django 2.2.1 on 2019-08-22 01:59

import FormsCustomize.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(upload_to='cars')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=FormsCustomize.models.content_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=120)),
                ('itemDesc', models.CharField(max_length=120)),
                ('itemPrice', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(default='Male', max_length=16)),
                ('age', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=32)),
                ('english', models.CharField(max_length=3)),
                ('nepali', models.CharField(max_length=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='FormsCustomize.Student')),
            ],
            options={
                'db_table': 'marks',
            },
        ),
    ]
