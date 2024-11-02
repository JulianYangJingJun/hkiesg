from wagtail.admin.ui.tables import Column
from wagtail.admin.views.generic import IndexView
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet
from .models import NewsArticle

class NewsArticleViewSet(SnippetViewSet):
    model = NewsArticle
    icon = "doc-full"
    menu_label = '文章管理'
    menu_order = 200
    list_display = ('title', 'publish_date', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'content')
    ordering = ['-publish_date']
    
    add_to_admin_menu = True
    
    list_display = {
        'title': Column(name='title', label="标题"),
        'publish_date': Column(name='publish_date', label="发布时间"),
        'is_published': Column(name='is_published', label="发布状态"),
    }

# 注册视图集
register_snippet(NewsArticle, viewset=NewsArticleViewSet) 