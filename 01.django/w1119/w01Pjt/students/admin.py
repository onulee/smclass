from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display = ['name','major','grade','age','gender','hobby']

admin.site.register(Student,StudentAdmin)
