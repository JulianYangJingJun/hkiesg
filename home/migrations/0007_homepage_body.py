# Generated by Django 4.2.16 on 2024-11-01 11:45

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_menu_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', 0), ('paragraph', 1), ('image', 2)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'full title'}), 1: ('wagtail.blocks.RichTextBlock', (), {}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {})}, default=1),
            preserve_default=False,
        ),
    ]