a_list = []
for i in range(25):
  a_list.append(i+1)

print(a_list)

b_list = []
a = []
for i in range(25):
  if i==0: 
    a.append(a_list[i])
    continue
  if i%5==0:
    b_list.append(a)
    a = []
    a.append(a_list[i])
  else:
    a.append(a_list[i])  

print(b_list)