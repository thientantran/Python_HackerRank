import itertools
k, m = (map(int, input().split()))

lst = []

for i in range(k):
    newLst = list(map(int, input().split()))
    a = lst.append(newLst[1:])

result = 0
newProduct = list(itertools.product(*lst))
for product in newProduct:
    result = max(sum([x*x for x in product])%m, result)

print(result)

