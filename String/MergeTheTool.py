def trung(string):
    kq = []
    for i in string:
        if (i in kq) == False:
            kq.append(i)
    return "".join(kq)
def merge_the_tools(string, k):
    import math
    for i in range(math.ceil(len(string)/k)):
        print(trung(string[i*k:i*k+k]))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)