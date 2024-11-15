from django.db import models

## db생성
class Student(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_grade = models.IntegerField(default=0)
  s_age = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)

  def __str__(self):
    return self.s_name