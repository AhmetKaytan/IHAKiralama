# Generated by Django 4.2.7 on 2023-12-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('agirlik', models.IntegerField()),
                ('kategori', models.CharField(max_length=150)),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
    ]
