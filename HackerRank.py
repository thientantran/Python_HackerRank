############# ---------------------function()

def is_leap(year):
    leap = False
    if year %4==0:
        leap=True
        if year%400==0: 
            leap=True
        elif year%100==0 and year%400!=0:
            leap=False
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))

###### ------------------------------itertools.combinations()

from itertools import combinations

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        #sorted(s) trả về list
        print(''.join(j))
        # join sử dụng cho list

####################################### BASIC DATA TYPES ###########################################################
####----------------List Comprehensions------------------

x = int(input())
y = int(input())
z = int(input())
n = int(input())
A=[]

for i in range(x+1):
    a=[0,0,0]
    a[0]=i
    for j in range(y+1):
        a[1]=j
        for k in range(z+1):
            a[2]=k    
            A.append(a)
            # tại sao khi thay đổi a thì A lại thay đổi theo a        
kq=[]
for i in range(len(A)):
    if sum(A[i])!=n:
        kq.append(A[i])
print(kq)

#answer
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

##################-----------------Find the Runner-Up Score!----------------
n = int(input())
arr = map(int, input().split())
arr=list(arr)
max=-101
for i in range(len(arr)):
    
    if max<arr[i]:
        max=arr[i]
kq=-101
for i in range(len(arr)):
    if kq<arr[i] and arr[i]<max:
        kq=arr[i]
print(kq)

######---------------------------------Nested Lists


A=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    A.append([name,score])
diem=[]
for i in range(len(A)):
    diem.append(A[i][1])
lowestDiem=min(diem)
diem.sort()
scLowestDiem=lowestDiem
for i in range(len(diem)):
    if diem[i]!=lowestDiem:
        scLowestDiem=diem[i]
        break
ten=[]
for i in range(len(A)):
    if A[i][1]==scLowestDiem:
        ten.append(A[i][0])

ten.sort()
for i in range(len(ten)):
    print(ten[i])


#####------------------- Lists --------------- Bai hay -------------------------
n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

#------------------------- finding the percentage---------------------------------
n = int(input())
student_marks = {} # tao 1 tuple
for _ in range(n):
    name, *line = input().split() # lay *line để lấy list tất cả các phần tử sau phần tử đầu tiên
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
a=student_marks[query_name]
b=sum(a)/3
print("%.2f" %b)