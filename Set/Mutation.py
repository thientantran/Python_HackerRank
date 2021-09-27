def mutation(setA, string, stringSet):
    lst = string.split()
    setB = set(map(int, stringSet.split()))
    if lst[0]=="intersection_update":
        setA.intersection_update(setB)
    elif lst[0]=="update":
        setA.update(setB)
    elif lst[0]=="symmetric_difference_update":
        setA.symmetric_difference_update(setB)
    elif lst[0]=="difference_update":
        setA.difference_update(setB)
    return setA
n = int(input())
a = set(map(int, input().split()))
m = int(input())
for i in range(m):
    lenh = input()
    daySo = input()
    a = mutation(a, lenh, daySo)
print(sum(a))
