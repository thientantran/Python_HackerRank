
s = input().strip()
k = input().strip()
ds = []
for i in range(len(s)-len(k)+1):

    # print(s[i:i+len(k)])
    if s[i:i+len(k)] == k:
        ds.append((i, i+len(k)-1))
if len(ds)==0:
    print((-1,-1))
else:
           
    for i in ds:
        print(i)
     