# Generated by Django 3.1.2 on 2020-11-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
