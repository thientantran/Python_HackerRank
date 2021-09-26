def average(array):
    lst = list(set(array))
    return sum(lst)/len(lst)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)