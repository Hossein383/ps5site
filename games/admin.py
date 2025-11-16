from django.contrib import admin
from . import models
@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name' , 'auther']
    search_fields = ['name']
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','time']
    search_fields = ['body']