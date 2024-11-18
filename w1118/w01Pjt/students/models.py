from django.db import models

# 객체선언 - db테이블 생성
class Student(models.Model):
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=0)
  age = models.IntegerField(default=0)
  gender = models.CharField(max_length=10)
  
  def __str__(self):
    return self.name
