# Generated by Django 3.2.6 on 2021-12-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('ucnic', models.CharField(max_length=13, unique=True)),
                ('uphone', models.CharField(max_length=100)),
                ('uemail', models.CharField(max_length=100, unique=True)),
                ('uaddress', models.CharField(max_length=100)),
                ('upassword', models.CharField(max_length=100)),
                ('urpassword', models.CharField(max_length=100)),
            ],
        ),
    ]