from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock, CharBlock,RawHTMLBlock,URLBlock,StructBlock,ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks  
from wagtail.blocks import PageChooserBlock
from wagtail.snippets.models import register_snippet




class HomePage(Page):
    banner_title1 = models.CharField(max_length=255, default="默认标题")
    banner_title2 = models.CharField(max_length=255, default="默认标题")
    middle_title = models.CharField(max_length=255, default="默认中间标题") 
    group_4 = StreamField([
        ('raw_html', RawHTMLBlock()),
    ], blank=True)  # 使用 StreamField 包含 RawHTMLBlock
    content_panels = Page.content_panels + [
        FieldPanel("banner_title1"),
        FieldPanel("banner_title2"),
        FieldPanel("middle_title"),
        FieldPanel("group_4")
    ] 
    
    pass

class AboutPage(Page):
    pass

class ServicesPage(Page):
    pass

class ActivitiesPage(Page):
    pass

class MembersPage(Page):
    pass

@register_snippet
class Logo(models.Model):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alt_text = models.CharField(max_length=100, blank=True, help_text="Logo的替代文本")

    panels = [
        FieldPanel('logo'),
        FieldPanel('alt_text'),
    ]

    def __str__(self):
        return self.alt_text or "Logo"

    class Meta:
        verbose_name = "网站Logo"
        verbose_name_plural = "网站Logo"
