# Generated by Django 5.0.6 on 2024-06-07 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('picture', models.CharField(max_length=500)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('job', models.CharField(choices=[('0', 'user'), ('2', 'author'), ('1', 'librarian'), ('3', 'admin')], max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('customUserFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customUserAuthorFK', to=settings.AUTH_USER_MODEL)),
                ('pictureFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customUserPictureFK', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pages', models.IntegerField()),
                ('format', models.TextField(choices=[('2', 'E-Book'), ('1', 'Fisico')], max_length=30)),
                ('edition', models.IntegerField()),
                ('releaseDate', models.DateField()),
                ('stats', models.CharField(choices=[('1', 'Pendente'), ('3', 'Aprovado'), ('2', 'Cancelado')], max_length=30)),
                ('stars', models.CharField(choices=[('4', '4'), ('2', '2'), ('3', '3'), ('5', '5'), ('1', '1')], max_length=30)),
                ('authorFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookAuthorFK', to=settings.AUTH_USER_MODEL)),
                ('categoryFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookCategoryFK', to='seraiva.category')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowingDate', models.DateField(auto_now=True)),
                ('devolutionDate', models.DateField()),
                ('returnedDate', models.DateTimeField(blank=True, null=True)),
                ('bookFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookFKBorrowing', to='seraiva.book')),
                ('userFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFKBorrowing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
