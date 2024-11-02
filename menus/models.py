from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, StructBlock, ListBlock, PageChooserBlock

class MenuItemBlock(StructBlock):
    title_zh = CharBlock(label="中文菜单名称")
    title_en = CharBlock(label="英文菜单名称")
    link_page_zh = PageChooserBlock(label="中文页面", required=False, can_choose_root=True)
    link_page_en = PageChooserBlock(label="英文页面", required=False, can_choose_root=True)
    sub_items = ListBlock(StructBlock([
        ('title_zh', CharBlock(label="中文子菜单名称")),
        ('title_en', CharBlock(label="英文子菜单名称")),
        ('link_page_zh', PageChooserBlock(label="中文页面", required=False)),
        ('link_page_en', PageChooserBlock(label="英文页面", required=False)),
    ]), label="子菜单项", required=False)

    class Meta:
        icon = 'link'

@register_snippet
class MainMenu(models.Model):
    menu_items = StreamField([
        ('menu_item', ListBlock(MenuItemBlock())),
    ], use_json_field=True)

    panels = [
        FieldPanel("menu_items"),
    ]

    def __str__(self):
        return "主导航菜单"

    class Meta:
        verbose_name = "主导航菜单"
        verbose_name_plural = "主导航菜单"