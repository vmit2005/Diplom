# Generated by Django 4.1.7 on 2023-06-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_alles_alter_feedback_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='alles',
            field=models.BooleanField(blank=True, default=True, verbose_name='Показывать всем '),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дата'),
        ),
    ]
