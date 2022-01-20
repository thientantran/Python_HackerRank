from collections import OrderedDict
ordered_dictionary = OrderedDict()

n =int(input())
for i in range(n):
    newList = input().split()
    
    itemName = " ".join(newList[:-1])
    itemQuantity = int(newList[-1])
    
    if itemName in ordered_dictionary:
        ordered_dictionary[itemName] = ordered_dictionary[itemName] + itemQuantity
    else:
        ordered_dictionary[itemName] = itemQuantity

for item in ordered_dictionary:
    print(f"{item} {ordered_dictionary[item]}")