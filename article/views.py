from typing import Dict, Any, Union
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse,Http404
from django.core.paginator import Paginator
from .models import Article,blogType
from comment.models import Comment
from comment.forms import CommentForm
from read_statistic.utils import read_once_read
# Create your views here.
def get_blog_list_common_data(request,blog_all_list):
    paginator = Paginator(blog_all_list, 3)  # 每8页分页
    page_num = request.GET.get('page', 1)  # 获取URL的页面参数
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # 获取当前页码
    # articles=Article.objects.filter(is_deleted=False)
    # 获取当前页码前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 省略页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 添加首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    # 获取日期数量
    blog_dates= Article.objects.dates('created_time','month',order="DESC")
    blog_dates_dict={}
    for blog_date in blog_dates:
        blog_count=Article.objects.filter(created_time__year=blog_date.year,
                                          created_time__month=blog_date.month)
        count=blog_count.count()
        blog_dates_dict[blog_date]=count
        print(count)

    context={}
    context['page_range'] = page_range
    context['blog_types'] = blogType.objects.annotate(blog_count=Count('article'))
                                                        # blogType.objects.all()
    context['page_of_blogs'] = page_of_blogs
    context['blog_dates'] = blog_dates_dict
    return context
def article_detail(request,article_id):
    # 阅读计数
    article= get_object_or_404(Article,pk=article_id)
    read_cookie_key = read_once_read(request,article)
    blog_content_type=ContentType.objects.get_for_model(article)
    comments=Comment.objects.filter(content_type=blog_content_type,object_id=article.pk,parent=None)
    context={}
    context['prevous_blog']=Article.objects.filter(created_time__gt=article.created_time).last()
    context['next_blog']=Article.objects.filter(created_time__lt=article.created_time).first()
    context['article_obj']=article
    context['comments']=comments.order_by('-comment_time')
    context['comment_form']=CommentForm(initial={'content_type':blog_content_type.model,'object_id':article_id,'reply_comment_id':0})
    response =  render(request, "article_detail.html", context)
    response.set_cookie(read_cookie_key,'true')
    return response

def article_list(request):
    blog_all_list=Article.objects.filter(is_deleted=False)
    context=get_blog_list_common_data(request,blog_all_list)
    # context['articles']=articles
    return render(request,"articles_list.html",context)
def blog_with_type(request,blogs_type_pk):
    blog_Type = get_object_or_404(blogType, pk=blogs_type_pk)
    blog_all_list = Article.objects.filter(blog_Type=blog_Type)
    context = get_blog_list_common_data(request,blog_all_list)
    context['blog_type']=blog_Type
    # context['articles']=Article.objects.filter(blog_Type=blog_Type)
    return render(request,"articles_type.html",context)
def blog_with_date(request,year,month):
    blog_all_list = Article.objects.filter(is_deleted=False,created_time__year=year,created_time__month=month)
    context=get_blog_list_common_data(request,blog_all_list)
    context['blog_with_date']='%s年%s月' %(year,month)
    return render(request,'blog_with_date.html',context)
