# fruit_list = ["kiwi", "apple", "melon", "banana", "orange"]
# onegi = 0

# for i in fruit_list:
#     if onegi < len(i):
#         onegi = (len(i))
#     print(onegi)
import random
n=5
p=[x for x in range(1,n**2+1)]
k=0
b=0
for i in range(n,n**2+1,n):
  k+=1
  if k%2==0:
    print(sorted(p[b:i],reverse=True))
  else:
    print(sorted(p[b:i]))
  b+=n