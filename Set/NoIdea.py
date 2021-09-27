t = input()
arr = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
kq=0
for i in arr:
    if i in like:
        kq+=1
    if i in dislike:
        kq+=-1
print(kq)