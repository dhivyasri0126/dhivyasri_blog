# Generated by Django 5.2.4 on 2025-07-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.CharField(default='Default', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
