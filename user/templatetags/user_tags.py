from django import template
from urllib.parse import urlencode

register=template.Library()

@register.simple_tag
def get_login_qq_url():
    params={
        'grant_type':'authorization_code',
        'client_id':'101860458',
        'client_secret':'9abbee61854cb6b801e0adf2e364823b',
        'code':'authorization_code',
        'redirect_uri':'http://127.0.0.1:8000/user/login_by_qq',
    }
    return 'https://graph.qq.com/oauth2.0/token?' +urlencode(params)