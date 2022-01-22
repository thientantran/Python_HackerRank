
nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())


newList = sorted(arr, key = lambda x : x[k])

# print(newList)
for athelete in newList:
    print(" ".join([str(n) for n in athelete]))