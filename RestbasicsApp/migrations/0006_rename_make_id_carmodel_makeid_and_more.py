# Generated by Django 4.1.1 on 2022-10-09 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestbasicsApp', '0005_carmodel_data_delete_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='Make_ID',
            new_name='MakeID',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='Make_Name',
            new_name='MakeName',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='Model_ID',
            new_name='ModelID',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='Model_Name',
            new_name='ModelName',
        ),
    ]