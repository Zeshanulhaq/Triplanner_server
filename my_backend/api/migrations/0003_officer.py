# Generated by Django 3.2.6 on 2021-12-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=100)),
                ('ocnic', models.CharField(max_length=13, unique=True)),
                ('ophone', models.CharField(max_length=100)),
                ('oemail', models.CharField(max_length=100, unique=True)),
                ('oaddress', models.CharField(max_length=100)),
                ('opassword', models.CharField(max_length=100)),
                ('orpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
