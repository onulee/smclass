from django.db import models

class Board(models.Model):
  # 게시판 번호
  bno = models.AutoField(primary_key=True)
  id = models.CharField(max_length=100)
  # member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  # 답글을 사용할때 그룹핑
  bgroup = models.IntegerField(null=True)
  # 답글을 사용할때 순서
  bstep = models.IntegerField(default=0)
  # 답글을 사용할때 들여쓰기
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.bno},{self.id},{self.btitle},{self.bdate}"