# Generated by Django 3.0.1 on 2021-07-09 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]