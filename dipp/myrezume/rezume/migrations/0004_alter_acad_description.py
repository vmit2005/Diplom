# Generated by Django 4.1.7 on 2023-05-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezume', '0003_alter_rezume_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acad',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
