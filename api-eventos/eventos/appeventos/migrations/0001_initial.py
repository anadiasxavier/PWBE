# Generated by Django 5.1.7 on 2025-03-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('datatime', models.DateTimeField()),
                ('local', models.CharField(blank=True, max_length=255)),
                ('categoria', models.CharField(choices=[('MÚSICA', 'Música'), ('PALESTRA', 'Palestra'), ('WORKSHOP', 'Workshop')], max_length=9)),
            ],
        ),
    ]
