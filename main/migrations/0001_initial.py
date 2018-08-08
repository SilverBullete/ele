# Generated by Django 2.0.3 on 2018-08-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cookies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleme_key', models.CharField(max_length=255)),
                ('url_appand', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('used_times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='kami',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kami', models.CharField(max_length=12)),
                ('val', models.IntegerField()),
                ('used', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('qq', models.CharField(max_length=11)),
                ('phone', models.CharField(max_length=11)),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
