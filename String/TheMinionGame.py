def minion_game(s):
    s = s.lower()
    stuartWord = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    kevinWord = ["u",'e','o','a','i']
    stuartNumber = 0
    kevinNumber = 0
    for i in range(len(s)):
        if s[i] in stuartWord:
            stuartNumber += (len(s)-i)
    
    for i in range(len(s)):
        if s[i] in kevinWord:
            kevinNumber += (len(s)-i)

    if stuartNumber > kevinNumber:
        print('Stuart',stuartNumber)
    elif stuartNumber < kevinNumber:
        print('Kevin',kevinNumber)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)