# Generated by Django 4.2 on 2023-07-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blog_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to='blogs/'),
        ),
    ]