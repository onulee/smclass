from django.contrib import admin
from board.models import Board
class BoardAdmin(admin.ModelAdmin):
  list_display = ['bno','id','btitle','bgroup','bdate']

admin.site.register(Board,BoardAdmin)
