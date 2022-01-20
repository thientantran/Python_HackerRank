# n = int(input())
# cols_list = input().split()
# index = cols_list.index("MARKS")
# total = 0
# for i in range(n):
#     total+=float((input().split())[index])
# print(total/n)


from collections import namedtuple
n = int(input())
row = namedtuple('row', input())
total = 0
for x in range(n):
    a,b,c,d = input().split()
    s = row(a,b,c,d)
    total += int(s.MARKS)
print(total/n)