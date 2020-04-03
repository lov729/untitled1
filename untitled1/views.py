import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Sum,Q
# 缓存
from django.core.cache import cache
from read_statistic.utils import get_day_read_num,get_day_hot_data,get_yes_hot_data
from django.contrib.contenttypes.models import ContentType
from article.models import Article
from django.utils import timezone

# Create your views here.
def get_week_hot_blog():
    today=timezone.now().date()
    date=today-datetime.timedelta(days=7)
    blogs=Article.objects\
                 .filter(read_detail__date__lt=today,read_detail__date__gte=date)\
                 .values('id','title')\
                 .annotate(read_num_sum=Sum('read_detail__read_num'))\
                 .order_by('-read_num_sum')
    return blogs[:7]

def home(request):
    blog_content_type= ContentType.objects.get_for_model(Article)
    dates,read_nums = get_day_read_num(blog_content_type)
    today_hot_dot=get_day_hot_data(blog_content_type)
    yes_hot_dot=get_yes_hot_data(blog_content_type)
    #获取七天热门文章缓存数据
    hot_blog_for_week=cache.get('hot_blog_for_week')
    if hot_blog_for_week is None:
        hot_blog_for_week=get_week_hot_blog()
        cache.set('hot_blog_for_week',get_week_hot_blog,3600)
    context={}
    context['today_hot_dot']=today_hot_dot
    context['yes_hot_dot']=yes_hot_dot
    context['hot_dot_week'] = hot_blog_for_week
    context['dates']=dates
    context['read_nums']=read_nums
    return render(request,'home.html',context)
def search(request):
    search_word=request.GET.get('wd','').strip()
    #分词:按空格|~
    condition=None
    for word in search_word.split(' '):
        if condition is None:
            condition=Q(title__icontains=word)
        else:
            condition=condition|Q(title__icontains=word)
    search_articles=[]
    if condition is not None:
        search_articles=Article.objects.filter(condition)
    #分页
    paginator = Paginator(search_articles, 3)  # 每8页分页
    page_num = request.GET.get('page', 1)  # 获取URL的页面参数
    page_of_blogs = paginator.get_page(page_num)
    context={}
    context['search_word']=search_word
    context['search_articles_count']=search_articles.count()
    context['search_articles']=search_articles
    context['page_of_blogs']=page_of_blogs
    return render(request,'search.html',context)



