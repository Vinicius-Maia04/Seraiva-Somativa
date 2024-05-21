# Generated by Django 5.0.6 on 2024-05-20 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seraiva', '0004_alter_book_format_alter_book_stars_alter_book_stats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='format',
            field=models.TextField(choices=[('2', 'E-Book'), ('1', 'Fisico')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='stars',
            field=models.CharField(choices=[('2', '2'), ('5', '5'), ('3', '3'), ('4', '4'), ('1', '1')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='stats',
            field=models.CharField(choices=[('3', 'Aprovado'), ('2', 'Cancelado'), ('1', 'Pendente')], max_length=30),
        ),
    ]
