# Generated by Django 3.2.9 on 2021-12-25 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_officer_ophone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='Officer',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='uaddress',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='uname',
            new_name='lname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ucnic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uphone',
        ),
    ]
