# Generated by Django 3.1.7 on 2021-04-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=120, null=True)),
                ('Unique_ID', models.CharField(max_length=70, null=True)),
                ('Email_ID', models.CharField(max_length=120, null=True)),
                ('Password', models.CharField(max_length=40, null=True)),
                ('Joining_Date', models.DateField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worksubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueID', models.CharField(max_length=70, null=True)),
                ('work_from', models.TimeField(null=True)),
                ('Work_Description', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=70)),
                ('work_to', models.TimeField(null=True)),
            ],
        ),
    ]
