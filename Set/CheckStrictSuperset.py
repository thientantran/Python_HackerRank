def checkSubset(setA, setB):
# setB co phai subset cua A
    if len(setA|setB) == len(setA):
        return True
    else:
        return False
def checkStrictSubset(setA, setB):
# setB co phai strich subset cua setB ko??
    if (checkSubset(setA, setB)) & (len(setA)>len(setB)):
        return True
    else:
        return False

a = set(map(int, input().split()))
n = int(input())
kq = True
for i in range(n):
    b = set(map(int, input().split()))
    if (checkStrictSubset(a,b)) == False:
        kq=False
        break
print(kq)