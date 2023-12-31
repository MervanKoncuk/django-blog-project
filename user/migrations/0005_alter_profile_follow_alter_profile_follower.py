# Generated by Django 4.2 on 2023-07-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_follow_profile_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='takip', to='user.profile', verbose_name='Takip Edilenler'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='takipciler', to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
