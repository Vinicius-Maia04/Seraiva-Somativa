# Generated by Django 5.0.6 on 2024-06-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seraiva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='format',
            field=models.TextField(choices=[('1', 'Fisico'), ('2', 'E-Book')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='stars',
            field=models.CharField(choices=[('1', '1'), ('4', '4'), ('2', '2'), ('5', '5'), ('3', '3')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='stats',
            field=models.CharField(choices=[('2', 'Cancelado'), ('3', 'Aprovado'), ('1', 'Pendente')], max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job',
            field=models.CharField(choices=[('1', 'librarian'), ('0', 'user'), ('2', 'author'), ('3', 'admin')], max_length=30),
        ),
    ]
