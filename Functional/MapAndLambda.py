cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        kq = [0,1]
        for i in range(2, n):
            nextNumber = kq[i-1] + kq[i-2]
            kq.append(nextNumber)
        return kq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))