# Generated by Django 4.2.16 on 2024-10-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_banner_title_homepage_middle_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_title',
            new_name='banner_title1',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title2',
            field=models.CharField(default='默认标题', max_length=255),
        ),
    ]