# Generated by Django 4.2 on 2023-07-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='isim',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='blogs/'),
        ),
    ]
