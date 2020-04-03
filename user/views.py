import json
from datetime import datetime
import string
import random
import time
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from untitled1.forms import loginForm,RegForm,ChangeNicknameForm,BondemailForm,ChangePasswordForm,ForgotPassword
from django.contrib import auth
from .models import Profile, Paper, Grade
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def userlogin(request):
 if request.method=='POST':
     login_form = loginForm(request.POST)
     if login_form.is_valid():
        user=login_form.cleaned_data['user']
        auth.login(request,user)
        return redirect(request.GET.get('from',reverse('home')))
 else:
         login_form = loginForm()
 context={}
 context['login_form']=login_form
 return render(request,'login.html',context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST,request=request)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email=reg_form.cleaned_data['email']
            password=reg_form.cleaned_data['password']
            user=User.objects.create_user(username,email,password)
            user.save()
            # 清除掉session
            del request.session['register_code']
            #注册后登陆
            user = auth.authenticate(username=username, password=password)
            auth.login(request,user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] =reg_form
    return render(request, 'register.html', context)
def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

def user_info(request):
    id=request.GET.get('id')
    integral=Profile.objects.get(id=id)
    context={}
    context['int']=integral
    return render(request,'user_info.html', context)
def change_nickname(request):
    refer=request.GET.get('from',reverse('home'))
    context={}
    if request.method=='POST':
        form=ChangeNicknameForm(request.POST,user=request.user)
        if form.is_valid():
            nickname_new=form.cleaned_data['nickname_new']
            profile,created=Profile.objects.get_or_create(user=request.user)
            profile.nickname=nickname_new
            profile.save()
            return redirect(refer)
    else:
        form=ChangeNicknameForm()
        context['form']=form
        context['page_title']='修改昵称'
        context['form_title']='修改昵称'
        context['submit_text']='修改'
        context['return_back_url']=refer
        return render(request,'form.html',context)
def bind_email(request):
    refer = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        form = BondemailForm(request.POST, request=request)
        if form.is_valid():
            if form.is_valid():
                email=form.cleaned_data['email']
                request.user.email=email
                request.user.save()
                del request.session['bind_email_code']
                return redirect(refer)
    else:
        form=BondemailForm()
    context={}
    context['page_title']='绑定邮箱'
    context['form_title'] = '绑定邮箱'
    context['submit_text'] = '绑定'
    context['form']=form
    context['return_back_url'] = refer
    return render(request,'bindemail.html',context)
def send_ver_code(request):
    email=request.GET.get('email','')
    data={}
    send_for=request.GET.get('send_for','')
    if email !='':
        code=''.join(random.sample(string.ascii_letters + string.digits,4))
        now=int(time.time())
        send_code_time=request.session.get('send_code_time',0)
        if now-send_code_time<30:
            data['status']='ERROR'
        else:
            request.session[send_for] = code
            request.session['send_code_time']=now
            send_mail(
                '欢迎您的加入',
                '验证码: %s' %code,
                '714882162@qq.com',
                [email],
                fail_silently = False,
            )
        data['status']='SUCCESS'
    else:
        data['status']='FALSE'
    return JsonResponse(data)
def change_password(request):
    if request.method=='POST':
        form=ChangePasswordForm(request.POST,user=request.user)
        if form.is_valid():
            user=request.user
            old_password=form.cleaned_data['old_password']
            new_password=form.cleaned_data['new_password']
            new_password_again=form.cleaned_data['new_password_again']
            user.set_password(new_password)
            user.save()
            auth.logout(request)
            return redirect(reverse('home'))
    else:
         form = ChangePasswordForm()
    context = {}
    context['form'] = form
    context['page_title'] = '修改密码'
    context['form_title'] = '修改密码'
    context['submit_text'] = '修改'
    context['return_back_url'] = request.GET.get('from',reverse('home'))
    return render(request, 'form.html', context)
def forgot_password(request):
    refer = reverse('login')
    if request.method == 'POST':
        form = ForgotPassword(request.POST, request=request)
        if form.is_valid():
            email=form.cleaned_data['email']
            new_password=form.cleaned_data['new_password']
            user=User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            del request.session['forgot_password_code']
            return redirect(refer)
    else:
        form=ForgotPassword()
    context={}
    context['page_title']='重置密码'
    context['form_title'] = '重置密码'
    context['submit_text'] = '重置'
    context['form']=form
    context['return_back_url'] = refer
    return render(request,'forgot_password.html',context)
def exam(request):
    exam=Paper.objects.all()
    data={}
    data['exam']=exam
    return render(request,'exam.html',data)
def examgrade(request):
    sid=request.POST.get('sid')
    user=User.objects.get(id=sid)
    # grade=Grade.objects.filter(sid=user.id)
    question = Paper.objects.all().values('pid').values('pid__id')
    grade = 0
    for p in question:
        qid = str(p['pid__id'])
        myans = request.POST.get(qid)
        ggd = int(myans)
        grade += ggd
        print(grade)
    if not Grade.objects.get(sid=user.pk):
        Grade.objects.create(sid_id=sid, grade=grade)
        print("1")
    mygrade = Grade.objects.get(sid=sid)
    mygrade.grade=grade
    mygrade.save()
    data={}
    data['grade']=mygrade
    if mygrade.grade > 1:
       return render(request,'low.html')
    return render(request, 'grade.html', grade)
def post(request):
    username = request.POST['user']
    print(username)
    user = Profile.objects.filter(id=username)
    now = datetime.now().strftime('%Y-%m-%d')
    for now_user in user:
        if str(now_user.check_time) != now:
           now_user.integral += 20
           now_user.check_time = now
           now_user.save()
           result = json.dumps({"status":"success", "msg":"签到成功"}, ensure_ascii=False)
        else:
           result = json.dumps({"status": "fail", "msg": "签到失败，今天已经签过了"}, ensure_ascii=False)
        return HttpResponse(result)