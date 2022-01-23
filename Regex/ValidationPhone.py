import re

n=int(input())
m = re.compile(r'^[7-9]\d{9}$')
for i in range(n):
    phone = input()
    kq =bool(re.match(m, phone))
    if kq:
        print("YES")
    else:
        print("NO")