from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,verbose_name='昵称')
    integral = models.IntegerField(default=0, verbose_name='积分')
    check_time = models.DateField(default='1970-01-01', verbose_name='签到时间')
    def __str__(self):
        return '<Profile:%s for %s>' %(self.nickname,self.user.username)
def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile=Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username
User.get_nickname_or_username=get_nickname_or_username
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length=30)
    optionB=models.CharField('B选项',max_length=30)
    optionC=models.CharField('C选项',max_length=30)
    optionD=models.CharField('D选项',max_length=30)

    class Meta:
        db_table='question'
        verbose_name='测试题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s>'%(self.title);
class Paper(models.Model):
    #题号pid 和题库为多对多的关系
    pid=models.ManyToManyField(Question)#多对多

    class Meta:
        db_table='paper'
        verbose_name='测试表'
        verbose_name_plural=verbose_name
class Grade(models.Model):#添加外键
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.sid,self.grade);

    class Meta:
        db_table='grade'
        verbose_name='分数'
        verbose_name_plural=verbose_name
