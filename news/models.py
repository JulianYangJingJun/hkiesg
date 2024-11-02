from django.db import models
from django.utils import timezone
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import TranslatableMixin
from wagtail.admin.panels import Panel
from wagtail.admin.panels import FieldPanel as WagtailFieldPanel

class NewsArticle(TranslatableMixin, models.Model):
    title = models.CharField("标题", max_length=200)
    subtitle = models.CharField("副标题", max_length=200, blank=True)
    content = RichTextField("内容")
    publish_date = models.DateTimeField("发布时间", default=timezone.now)
    is_published = models.BooleanField("是否发布", default=False)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="封面图片"
    )
    
    panels = [
        MultiFieldPanel([
            WagtailFieldPanel('title'),
            WagtailFieldPanel('subtitle'),
            WagtailFieldPanel('featured_image'),
        ], heading="基本信息"),
        WagtailFieldPanel('content'),
        MultiFieldPanel([
            WagtailFieldPanel('publish_date'),
            WagtailFieldPanel('is_published'),
        ], heading="发布设置")
    ]
    
    class Meta:
        verbose_name = "动态文章"
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']
        constraints = [
            models.UniqueConstraint(
                fields=['translation_key', 'locale'],
                name='unique_translation_key_locale_news_newsarticle'
            )
        ]
    
    def __str__(self):
        return self.title
