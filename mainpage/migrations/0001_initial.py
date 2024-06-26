# Generated by Django 5.0.3 on 2024-03-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
