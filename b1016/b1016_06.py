import os

# mkdir : 현재 폴더만 생성
# makedirs : 현재폴더,하위폴더까지 생성
# os.path.exists() : 현재가 폴더가 존재하는지 확인

# 폴더가 없을시 폴더 생성
if not os.path.exists("c:/ddd"):
  os.makedirs("c:/ddd")

f = open("c:/ddd/c.txt","w",encoding="utf-8")
f.write("안녕하세요")
f.close()