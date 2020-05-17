# Generated by Django 3.0.2 on 2020-05-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Автор')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Authors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория ')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Books/', verbose_name='Изображение')),
                ('year', models.PositiveSmallIntegerField(default=0, verbose_name='Год издания')),
                ('cost', models.IntegerField(default=0, verbose_name='Цена')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author', verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]