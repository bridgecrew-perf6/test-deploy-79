# Generated by Django 3.2.4 on 2021-06-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_content_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
