# Generated by Django 5.1.7 on 2025-04-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0002_rename_apelido_usuariods16_biografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariods16',
            name='idade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
