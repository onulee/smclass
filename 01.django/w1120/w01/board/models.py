from django.db import models

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  id = models.CharField(max_length=100)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.btitle
