from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsArticle

# Create your views here.

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    
    def get_queryset(self):
        return NewsArticle.objects.filter(
            is_published=True
        ).order_by('-publish_date')

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
