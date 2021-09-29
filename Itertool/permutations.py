from itertools import permutations
lst= input().split()
a = (list(permutations(sorted(lst[0]), int(lst[1]))))

for i in a:
    print("".join(i))