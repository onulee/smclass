from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','pw','name','nicName','mdate']

# admin.site.register(Member,MemberAdmin)