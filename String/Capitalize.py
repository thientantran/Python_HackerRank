import os
def solve(s):
    tan = s.split(" ");
    kq=[]
    for i in tan:
        i=i.capitalize()
        kq.append(i)

    return (" ".join(kq))
if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    
    print(result)