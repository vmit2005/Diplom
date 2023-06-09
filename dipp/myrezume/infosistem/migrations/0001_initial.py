# Generated by Django 4.1.7 on 2023-05-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcopybook', models.IntegerField()),
                ('l1', models.BooleanField(blank=True, null=True)),
                ('l2', models.BooleanField(blank=True, null=True)),
                ('l3', models.BooleanField(blank=True, null=True)),
                ('l4', models.BooleanField(blank=True, null=True)),
                ('l5', models.BooleanField(blank=True, null=True)),
                ('l6', models.BooleanField(blank=True, null=True)),
                ('l7', models.BooleanField(blank=True, null=True)),
                ('l8', models.BooleanField(blank=True, null=True)),
                ('l9', models.BooleanField(blank=True, null=True)),
                ('l10', models.BooleanField(blank=True, null=True)),
                ('l11', models.BooleanField(blank=True, null=True)),
                ('l12', models.BooleanField(blank=True, null=True)),
                ('l13', models.BooleanField(blank=True, null=True)),
                ('l14', models.BooleanField(blank=True, null=True)),
                ('l15', models.BooleanField(blank=True, null=True)),
                ('l16', models.BooleanField(blank=True, null=True)),
                ('l17', models.BooleanField(blank=True, null=True)),
                ('l18', models.BooleanField(blank=True, null=True)),
                ('l19', models.BooleanField(blank=True, null=True)),
                ('l20', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aonn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcopybook', models.IntegerField()),
                ('o1', models.BooleanField(blank=True, null=True)),
                ('o2', models.BooleanField(blank=True, null=True)),
                ('o3', models.BooleanField(blank=True, null=True)),
                ('o4', models.BooleanField(blank=True, null=True)),
                ('o5', models.BooleanField(blank=True, null=True)),
                ('o6', models.BooleanField(blank=True, null=True)),
                ('o7', models.BooleanField(blank=True, null=True)),
                ('o8', models.BooleanField(blank=True, null=True)),
                ('o9', models.BooleanField(blank=True, null=True)),
                ('o10', models.BooleanField(blank=True, null=True)),
                ('o11', models.BooleanField(blank=True, null=True)),
                ('o12', models.BooleanField(blank=True, null=True)),
                ('o13', models.BooleanField(blank=True, null=True)),
                ('o14', models.BooleanField(blank=True, null=True)),
                ('o15', models.BooleanField(blank=True, null=True)),
                ('o16', models.BooleanField(blank=True, null=True)),
                ('o17', models.BooleanField(blank=True, null=True)),
                ('o18', models.BooleanField(blank=True, null=True)),
                ('o19', models.BooleanField(blank=True, null=True)),
                ('o20', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Copybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.CharField(max_length=127)),
                ('title', models.CharField(max_length=127)),
                ('url', models.URLField(blank=True)),
                ('n1', models.CharField(blank=True, max_length=8, null=True)),
                ('n2', models.CharField(blank=True, max_length=8, null=True)),
                ('n3', models.CharField(blank=True, max_length=8, null=True)),
                ('n4', models.CharField(blank=True, max_length=8, null=True)),
                ('n5', models.CharField(blank=True, max_length=8, null=True)),
                ('n6', models.CharField(blank=True, max_length=8, null=True)),
                ('n7', models.CharField(blank=True, max_length=8, null=True)),
                ('n8', models.CharField(blank=True, max_length=8, null=True)),
                ('n9', models.CharField(blank=True, max_length=8, null=True)),
                ('n10', models.CharField(blank=True, max_length=8, null=True)),
                ('n11', models.CharField(blank=True, max_length=8, null=True)),
                ('n12', models.CharField(blank=True, max_length=8, null=True)),
                ('n13', models.CharField(blank=True, max_length=8, null=True)),
                ('n14', models.CharField(blank=True, max_length=8, null=True)),
                ('n15', models.CharField(blank=True, max_length=8, null=True)),
                ('n16', models.CharField(blank=True, max_length=8, null=True)),
                ('n17', models.CharField(blank=True, max_length=8, null=True)),
                ('n18', models.CharField(blank=True, max_length=8, null=True)),
                ('n19', models.CharField(blank=True, max_length=8, null=True)),
                ('n20', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcopybook', models.IntegerField()),
                ('number', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=127)),
                ('a1', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a2', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a3', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a4', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a5', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a6', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a8', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a9', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a10', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a11', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a12', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a13', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a14', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a15', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a16', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a17', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('a18', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('t19', models.CharField(blank=True, max_length=127, null=True)),
                ('t20', models.CharField(blank=True, max_length=127, null=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
