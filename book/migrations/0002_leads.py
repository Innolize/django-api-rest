# Generated by Django 3.1.7 on 2021-03-08 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.library')),
            ],
        ),
    ]
