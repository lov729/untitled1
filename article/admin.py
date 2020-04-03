from django.contrib import admin
from .models import Article ,blogType
# Register your models here.
@admin.register(blogType)
class blogTypeAdmin(admin.ModelAdmin):
    list_display = ("id","type_name")
@admin.register(Article)
class ArcticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","blog_Type","author","get_read_num","created_time","last_updated_time","is_deleted")
    ordering = ("id",)
# admin.site.register(Article,ArcticleAdmin)