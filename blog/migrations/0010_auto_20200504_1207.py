# Generated by Django 3.0.4 on 2020-05-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200503_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Add an image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Add a video'),
        ),
    ]
