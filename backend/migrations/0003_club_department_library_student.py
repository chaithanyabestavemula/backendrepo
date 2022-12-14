# Generated by Django 3.2.16 on 2022-10-26 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20221017_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acesscard', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('acesscard', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.library')),
                ('club', models.ManyToManyField(to='backend.club')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.department')),
            ],
        ),
    ]
