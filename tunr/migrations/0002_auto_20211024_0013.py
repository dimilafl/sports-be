# Generated by Django 3.2.8 on 2021-10-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soccer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
