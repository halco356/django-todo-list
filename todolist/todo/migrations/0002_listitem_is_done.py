# Generated by Django 3.0 on 2020-07-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='is_done',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
