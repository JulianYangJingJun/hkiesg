# Generated by Django 4.2.16 on 2024-11-01 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['-publish_date'], 'verbose_name': '动态文章', 'verbose_name_plural': '动态文章'},
        ),
    ]