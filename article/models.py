from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistic.models import ReadNumExpand,ReadDetail
# Create your models here.
class blogType(models.Model):
    type_name = models.CharField(max_length=15,default="随笔")
    def __str__(self):
        return self.type_name

class Article(models.Model,ReadNumExpand):
    title=models.CharField(max_length=30)
    blog_Type=models.ForeignKey(blogType,on_delete=models.CASCADE)
    content= RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time=models.DateTimeField(auto_now=True)
    read_detail=GenericRelation(ReadDetail)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    is_deleted=models.BooleanField(default=False)
    #avatar=models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    def get_url(self):
        return reverse('article_detail',kwargs={'article_id':self.pk})
    def get_user(self):
        return self.author
    def __str__(self):
        return "<Article: %s>" % self.title
    class Meta:
        ordering =['-created_time']