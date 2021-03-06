# Generated by Django 3.2.3 on 2022-03-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Position', models.CharField(max_length=400)),
                ('Contact', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('about', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('color', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('short', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]
