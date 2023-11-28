# Generated by Django 4.2.7 on 2023-11-28 19:52

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
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.TextField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]