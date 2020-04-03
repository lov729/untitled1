from django.urls import reverse
from .models import Comment
from .forms import CommentForm
import json
from  django.http import JsonResponse
# Create your views here.

def update_comment(request):
    #解析当前地址，并重定向
    refer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)
    data = {}
    if comment_form.is_valid():

        #保存评论
        comment=Comment()
        comment.user=comment_form.cleaned_data['user']
        comment.text=comment_form.cleaned_data['text']
        comment.content_object=comment_form.cleaned_data['content_object']
        parent=comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root=parent.root if not parent.root is None else parent
            comment.parent=parent
            comment.reply_to=parent.user
        comment.save()

        #return redirect(refer) 未使用ajax 直接重定向
        data['status']='SUCCESS'
        data['username']=comment.user.get_nickname_or_username()
        data['comment_time']=comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text']=comment.text
        if not parent is None:
            data['reply_to']=comment.reply_to.get_nickname_or_username()
        else:
            data['reply_to']=''
        data['pk']=comment.pk
        data['root_pk']=comment.root.pk if not comment.root is None else ''
    else:

        data['status']='ERROR'
        data['message']=list(comment_form.errors.values())[0][0]
        #return render(request,'error.html',{'message':comment_form.errors,'redirect_to':refer})
    return JsonResponse(data)

