# Generated by Django 4.2.7 on 2023-11-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Remedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('brandId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicine.article')),
            ],
        ),
    ]
