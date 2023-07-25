# Generated by Django 4.2.3 on 2023-07-24 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MasterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('tanggal', models.DateField()),
                ('deskripsi', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edirektoriapjiiapps.masterkategori')),
            ],
        ),
    ]
