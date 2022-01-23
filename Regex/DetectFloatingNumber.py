import re

pattern = re.compile('^[-+]?\d*\.\d+$')
n = int(input())
for i in range(n):
    kq = pattern.match(input())
    print(bool(kq))