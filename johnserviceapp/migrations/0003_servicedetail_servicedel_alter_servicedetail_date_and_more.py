# Generated by Django 4.0.4 on 2022-08-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johnserviceapp', '0002_ownermain'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='servicedel',
            field=models.CharField(max_length=150, null='true'),
            preserve_default='true',
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='date',
            field=models.DateField(null='true'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='uname',
            field=models.CharField(max_length=50, null='true'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='vname',
            field=models.CharField(max_length=50, null='true'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='vnumber',
            field=models.CharField(max_length=50, null='true'),
        ),
    ]