# Generated by Django 3.2.18 on 2023-04-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20230420_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='data_started_reading',
            field=models.DateField(blank=True, default='unread'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_finished_reading',
            field=models.DateField(blank=True, default='unread'),
        ),
    ]
