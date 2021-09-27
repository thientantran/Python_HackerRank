def testCase(setA, setB):
    if len(setA|setB) == len(setA):
        return True
    else:
        return False
n = int(input())
for i in range(n):
    t = input()
    a = set(map(int, input().split()))
    t = input()
    b = set(map(int, input().split()))
    print(testCase(b,a))