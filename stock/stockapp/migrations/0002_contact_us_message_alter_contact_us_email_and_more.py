# Generated by Django 4.2.5 on 2023-09-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='message',
            field=models.TextField(default='hello'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
