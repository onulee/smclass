from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = ['id']
  # list_display = ['id','pw','name','nicname','cdate']

admin.site.register(Member,MemberAdmin)