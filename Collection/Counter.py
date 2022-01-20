x = int(input())
shoeSize = list(map(int, input().split()))
n= int(input())
total = 0
for i in range(n):
    size, price = list(map(int, input().split()))
    if size in shoeSize:
        total = total + price
        shoeSize.remove(size)
print(total)