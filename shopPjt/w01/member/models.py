from django.db import models

class Member(models.Model):
  # id,pw,name,nicName,phone,gender,hobby,mdate
  id = models.CharField(max_length=100,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100)
  phone = models.CharField(max_length=20,default="010-0000-0000")
  gender = models.CharField(max_length=10, default="남자")
  hobby = models.CharField(max_length=100,default="게임")
  mdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.id},{self.name},{self.nicName},{self.mdate}"