import itertools
n = int(input())
a = input().split()
k = int(input())

combinationList = list(itertools.combinations(a, k))
aList = [t for t in combinationList if "a" in t]
tan = (len(aList)/len(combinationList))
print("{:.4f}".format(tan))