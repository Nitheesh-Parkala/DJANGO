# Generated by Django 5.1.1 on 2024-10-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=40)),
                ('ephone_no', models.IntegerField()),
                ('esal', models.FloatField()),
                ('eplace', models.CharField(max_length=50)),
                ('ejob', models.CharField(max_length=40)),
            ],
        ),
    ]
