# get value from platform
n, m = map(int, input().split()) 


# n = int(input())
# m = n*3
tan = ".|."

for i in range(1,n,2):
    print(f"{tan*i}".center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
    print(f"{tan*i}".center(m,"-"))
