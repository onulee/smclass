import copy
name = ["홍길동","유관순","이순신"]
score = [100,90,95]

n_dic = dict(zip(name,score))

# a = n_dic #얕은 복사
a = copy.deepcopy(n_dic) # 깊은 복사

a['홍길동'] = 0
print(a)
print(n_dic)



# 얕은 복사
# name = ["홍길동","유관순","이순신"]
# n = name # name의 값을 n에 복사

# n[2] = "김구"
# print(n) # n의 이순신-> 김구로 변경

# print(name) # name의 이순신 -> 김구로 변경

# 깊은 복사
# name = ["홍길동","유관순","이순신"]

# # n = name #얕은 복사
# n = name[:] # 깊은 복사
# n[2] = "김구"  #깊은 복사를 하면, n의 리스트만 변경
# print(n)
# print(name)