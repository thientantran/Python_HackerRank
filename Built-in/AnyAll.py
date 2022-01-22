n = int(input())
newList = list(map(int, input().split()))
if all([i >= 0 for i in newList]):
    if any(str(j) == str(j)[::-1] for j in newList):
        print(True)
    else:
        print(False)
else:
    print(False)
