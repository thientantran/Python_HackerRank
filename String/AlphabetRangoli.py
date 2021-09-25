def print_rangoli(size):
    n = size
    import string

    letter=(list(string.ascii_lowercase))

    m = (n*2-1)+(n*2-2)
    def mang(n):
        tan=['0']
        t = letter[:n]
        tan.extend(t)
        lst =[]
        a = []
        result=[]
        for i in range(n, 0,-1):
            lst.append(tan[i])
            a = lst[:-1]
            a=a[::-1]
            # print(lst, a)
            resultList = []
            for j in lst:
                resultList.append(j)
            for t in a:
                resultList.append(t)
            # result.append(resultList)
            result.append("-".join(resultList).center(m,"-"))
        return result

    result = mang(n)
    for i in result:
        print(i)

    for i in result[:-1][::-1]:
        print(i)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)