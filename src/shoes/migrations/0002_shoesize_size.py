# Generated by Django 3.1.3 on 2023-11-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoesize',
            name='size',
            field=models.IntegerField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
