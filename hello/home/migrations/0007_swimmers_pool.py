# Generated by Django 3.2.7 on 2021-10-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swimmers_pool',
            fields=[
                ('swimmer_id', models.AutoField(primary_key=True, serialize=False)),
                ('swimmer_name', models.CharField(max_length=2000)),
                ('swimmer_tags', models.CharField(max_length=100)),
                ('swimmer_image', models.ImageField(upload_to='images')),
                ('swimmer_event', models.FileField(upload_to='images')),
            ],
        ),
    ]