def Ham(string):
    return string.split()

n = int(input())
a= set(map(int, input().split()))
N = int(input())

for i in range(N):
    tan = Ham(input())
    if tan[0]=="pop":
        a.pop()
    elif tan[0] == 'discard':
        a.discard(int(tan[1]))
    elif tan[0] == 'remove':
        a.remove(int(tan[1]))

print(sum(a))