# Generated by Django 4.2 on 2023-07-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takip Edilenler'),
        ),
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
