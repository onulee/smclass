from django.db import models
from member.models import Member

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True) # 게시글 번호
  member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True) # id
  # 좋아요
  like_members = models.ManyToManyField(Member,default="",related_name="like_member" )
  btitle = models.CharField(max_length=1000) # 
  bcontent = models.TextField()
  #계층형게시판에 필요
  bgroup = models.IntegerField(null=True) # 답글 그룹핑
  bstep = models.IntegerField(default=0) # 리스트 출력순서
  bindent = models.IntegerField(default=0) # 들여쓰기

  bhit = models.IntegerField(default=0) # 조회수
  bdate = models.DateTimeField(auto_now=True) # 작성일
  bfile = models.ImageField(null=True,blank=True)

  def __str__(self):
    return f"{self.bno},{self.btitle},{self.bdate}"