############# ---------------------function()

def is_leap(year):
    leap = False
    if year %4==0:
        leap=True
        if year%400==0: 
            leap=True
        elif year%100==0 and year%400!=0:
            leap=False
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))

###### ------------------------------itertools.combinations()

from itertools import combinations

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        #sorted(s) trả về list
        print(''.join(j))
        # join sử dụng cho list

