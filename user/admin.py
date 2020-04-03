from django.contrib import admin
from .models import Profile, Question, Paper, Grade
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('id','username','nickname','email','is_staff','is_active')
    def nickname(self,obj):
        return obj.profile.nickname
    nickname.short_description = '昵称'
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','nickname','integral','check_time',)
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display_ = ('pid',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','title','optionA','optionB','optionC','optionD')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id','sid','grade')