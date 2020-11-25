# Generated by Django 3.1.3 on 2020-11-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='book_num',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
