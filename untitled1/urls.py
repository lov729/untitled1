"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from article.views import article_detail,article_list,blog_with_type,blog_with_date
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('user/',include('user.urls')),
    path('comment/',include('comment.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('article/<int:article_id>', article_detail,name="article_detail"),
    path('articlelist/', article_list,name="article_list"),
    path('type/<int:blogs_type_pk>', blog_with_type,name="blog_with_type"),
    path('date/<int:year>/<int:month>',blog_with_date,name="blog_with_date"),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('my_notifications/',include('my_notifications.urls')),
    path('search/',views.search,name='search'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)