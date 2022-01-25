import re
n = int(input())
for i in range(n):
    s = input()
    match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
    for i in match_result:
        if i != '':
            print(i)

# for i in range(n):
#     s=input()

#     x=s.split()

#     if len(x)>1  and  '{' not in x:
#         x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
#         [print(i) for  i in x]