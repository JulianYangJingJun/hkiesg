# Generated by Django 4.2.16 on 2024-11-01 12:46

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homepage_menu_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_items', wagtail.fields.StreamField([('menu_item', 7)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'label': '菜单名称'}), 1: ('wagtail.blocks.PageChooserBlock', (), {'can_choose_root': True, 'label': '选择页面', 'required': False}), 2: ('wagtail.blocks.CharBlock', (), {'label': '子菜单名称'}), 3: ('wagtail.blocks.PageChooserBlock', (), {'label': '选择页面', 'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 2), ('link_page', 3)]], {}), 5: ('wagtail.blocks.ListBlock', (4,), {'label': '子菜单项', 'required': False}), 6: ('wagtail.blocks.StructBlock', [[('title', 0), ('link_page', 1), ('sub_items', 5)]], {}), 7: ('wagtail.blocks.ListBlock', (6,), {})})),
            ],
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='menu_items',
        ),
    ]
