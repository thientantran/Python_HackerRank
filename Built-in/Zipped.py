# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x = list(map(int, input().split()))
A = list()
for i in range(x):
    newList = list(map(eval, input().split()))
    A = A + [newList]
A = list(zip(*A))
B = [sum(i)/x for i in A]
for i in B:
    print(round(i,1))

