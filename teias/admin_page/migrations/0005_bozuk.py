# Generated by Django 2.2.2 on 2019-08-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0004_depo'),
    ]

    operations = [
        migrations.CreateModel(
            name='bozuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TUR', models.CharField(max_length=100)),
                ('MARKA', models.CharField(max_length=100)),
                ('MODEL', models.CharField(max_length=100)),
                ('SERI_NO', models.CharField(max_length=100)),
                ('DURUM', models.CharField(max_length=100)),
            ],
        ),
    ]
