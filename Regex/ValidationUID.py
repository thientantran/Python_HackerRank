# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
upperCheck = r'.*([A-Z].*){2,}'
digitCheck = r'.*([0-9].*){3,}'
alphanumericCheck = r'([A-Za-z0-9]){10}$'
repeatCheck = r'.*(.).*\1'

for i in range(n):
    s = input().strip()
    upperResult = bool(re.match(upperCheck, s))
    digitResut = bool(re.match(digitCheck, s))
    alphanumericResult = bool(re.match(alphanumericCheck,s))
    repeatResult = bool(re.match(repeatCheck,s))
    
    if upperResult and digitResut and alphanumericResult and not repeatResult:
        print("Valid")
    else:
        print("Invalid")

# for _ in range(int(input())):
#     u = ''.join(sorted(input()))
#     try:
#         assert re.search(r'[A-Z]{2}', u)
#         assert re.search(r'\d\d\d', u)
#         assert not re.search(r'[^a-zA-Z0-9]', u)
#         assert not re.search(r'(.)\1', u)
#         assert len(u) == 10
#     except:
#         print('Invalid')
#     else:
#         print('Valid')
