# Generated by Django 4.2.7 on 2023-12-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IHA', '0002_musteri_kiralama'),
    ]

    operations = [
        migrations.AddField(
            model_name='kiralama',
            name='kiralama_saati',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='musteri',
            name='telefon_no',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
