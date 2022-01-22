from django.views.generic import ListView, DetailView
from .models import  News
from datetime import datetime

class NewssList(ListView):
    model = News
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_post'] = datetime.utcnow()
        context['value1'] = None
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'flatpages/news_2.html'
    context_object_name = 'news_2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_news'] = datetime.utcnow()
        return context