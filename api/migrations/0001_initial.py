# Generated by Django 4.2.8 on 2023-12-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittleTask', models.CharField(max_length=50)),
                ('descriptionTask', models.CharField(max_length=200)),
                ('priorityTask', models.PositiveBigIntegerField()),
            ],
        ),
    ]
