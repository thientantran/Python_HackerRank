##FIRST WAY--------------------------------

# from collections import Counter

# wordList = []
# n = int(input())
# for i in range(n):
#     wordList.append(input())
# wordCounter = Counter(wordList)
# print(wordCounter)
# print(len(wordCounter))
# for word in wordCounter:
#     print(wordCounter[word],end=' ')

## SECOND WAY-------------------------------

from collections import OrderedDict
ordered_dictionary = OrderedDict()
n =int(input())
for i in range(n):
    word = input()
    if word in ordered_dictionary:
        ordered_dictionary[word] = ordered_dictionary[word] + 1
    else:
        ordered_dictionary[word] = 1

print(len(ordered_dictionary))
for word in ordered_dictionary:
    print(ordered_dictionary[word], end=" ")