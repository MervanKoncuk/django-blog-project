# Generated by Django 4.2 on 2023-07-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_blog_created_at_blog_owner_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
