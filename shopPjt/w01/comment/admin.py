from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
  list_display = ['cno','ccontent','cdate']

# Register your models here.
admin.site.register(Comment,CommentAdmin)