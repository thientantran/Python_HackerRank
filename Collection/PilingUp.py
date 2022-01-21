from collections import deque


def pile(numberList):
    
    numberDeque = deque(numberList)
    kq = "Yes"
    topNumber = (2**31) + 1
    while kq=="Yes" and len(numberDeque)>0: 
        if (numberDeque[-1] >= numberDeque[0]) and (topNumber >= numberDeque[-1]) :
            topNumber = numberDeque.pop()

        elif (numberDeque[-1] < numberDeque[0]) and (topNumber >= numberDeque[0]) :
            topNumber = numberDeque.popleft()

        else:

            kq ="No"

    return kq
t = int(input())
for i in range(t):
    n = int(input())
    numberList = list(map(int, input().split()))
    print(pile(numberList))

# print(pile([1,3,2]))