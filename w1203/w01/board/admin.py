from django.contrib import admin
from board.models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
  list_display = ['bno','btitle','bgroup','bdate']