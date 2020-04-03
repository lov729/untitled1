from django.urls import path
from . import views
urlpatterns=[
    path('userlogin/',views.userlogin,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('userinfo/',views.user_info,name='user_info'),
    path('changenick/',views.change_nickname,name='changenick'),
    path('bindemail/',views.bind_email,name='bindemail'),
    path('bind_code/',views.send_ver_code,name='bind_code'),
    path('change_password',views.change_password,name='change_password'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('exam/',views.exam,name='exam'),
    path('examgrade/',views.examgrade,name='examgrade'),
    path('check/',views.post,name='check'),
]