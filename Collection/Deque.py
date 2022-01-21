from collections import deque
n = int(input())
d = deque()
for i in range(n):
    newList = list(input().strip().split())
    command = newList[0]
    if command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
    elif command == 'append':
        d.append(int(newList[1]))
    elif command == 'appendleft':
        d.appendleft(int(newList[1]))
for i in d:
    print(i,end=' ')