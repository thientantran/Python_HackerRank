from collections import defaultdict

d = defaultdict(list)

n,m = list(map(int, input().split()))
#5,2
for i in range(n):
    d[input()].append(str(i+1))
    #(a, [1,2,4])
    #(b, [3,5]) 
for j in range(m):
    print(" ".join(d[input()]) or -1)