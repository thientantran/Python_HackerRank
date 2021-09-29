from itertools import combinations_with_replacement
lst= input().split()
a = (list(combinations_with_replacement(sorted(lst[0]), int(lst[1]))))

for i in a:
    print("".join(i))