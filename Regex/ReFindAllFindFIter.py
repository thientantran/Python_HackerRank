import re
# print(re.findall(r'\w','http://www.hackerrank.com/'))
# print(list(map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))))

s=input()
result = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)
