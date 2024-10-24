lists = ['10억','9억5,000','11억 500','7억','12억 5,250']

# 숫자로 변경하는 방법
def num_chg(p):
  b = p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0  
  price = f_num+s_num
  return price

#-------
r_list = list(map(num_chg,lists))
print(r_list)










# for list in lists:
#   a = list.split("억")
#   first_n = int(a[0].strip())*100000000
#   second_n = a[1].strip()
#   if second_n != '':
#     second_n = int(second_n.replace(",",""))*10000
#   else:
#     second_n = 0
#   print(f"실제금액 : {first_n+second_n:,}")