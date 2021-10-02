import itertools
a = input().strip()
group = []
key = []
for k, g in itertools.groupby(a):
    group.append(list(g))
    key.append(k)

for i in range(len(group)):
    print(tuple(((len(group[i])),int(key[i]))), end=" ")

    # print(tuple(len(group[i], key[i])), end=" ")
