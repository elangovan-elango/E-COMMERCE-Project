# Generated by Django 4.2.7 on 2023-11-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cateory',
            new_name='catagory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cateory',
            new_name='category',
        ),
    ]
