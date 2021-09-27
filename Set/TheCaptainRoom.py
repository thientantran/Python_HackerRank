k = int(input())
lst = list(map(int, input().split()))
a = set(lst)
diff = k*sum(a) - sum(lst)
for i in a:
    if diff == (k-1)*i:
        print(i)
        break