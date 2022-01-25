import re
n = int(input())

for i in range(n):
    inputText = input()
    inputText = re.sub(r'(?<= )(&&)(?= )',"and",inputText)
    inputText = re.sub(r'(?<= )(\|\|)(?= )',"or",inputText)
    print(inputText)