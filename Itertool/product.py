# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lst = ((list(product(A,B))))
a = [str(i) for i in lst]
print(" ".join(a))