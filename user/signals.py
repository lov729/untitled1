
from notifications.signals import notify
from django.db.models.signals import post_save
from django.dispatch import receiver
from  django.urls import reverse
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def send_notification(sender,instance,**kwargs):
    # 发送站内消息
    if kwargs['created']==True:
        verb='欢迎您的加入'
        url = reverse('user_info')
        notify.send(instance.user, recipient=instance, verb=verb, action_object=instance,url=url)