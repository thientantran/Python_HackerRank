"""
    Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
    str.isalnum()
    This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    str.isalpha()
    This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    str.isdigit()
    This method checks if all the characters of a string are digits (0-9).
    str.islower()
    This method checks if all the characters of a string are lowercase characters (a-z).
    str.isupper()
    This method checks if all the characters of a string are uppercase characters (A-Z).
"""

class StringValidators:
    def __init__(self, string):
        self.string = string
    
    def isAnyAlphaNumber(self):
        for i in self.string:
            if i.isalnum() == True:
                return True
        return False
    def isAnyAlpha(self):
        for i in self.string:
            if i.isalpha() == True:
                return True
        return False    
    def isAnyDigit(self):
        for i in self.string:
            if i.isdigit() == True:
                return True
        return False    
    
    def isAnyLower(self):
        for i in self.string:
            if i.islower() == True:
                return True
        return False
    
    def isAnyUpper(self):
        for i in self.string:
            if i.isupper() == True:
                return True
        return False
    
if __name__ == '__main__':
    s= input()
    S = StringValidators(s)
    print(S.isAnyAlphaNumber())
    print(S.isAnyAlpha())
    print(S.isAnyDigit())
    print(S.isAnyLower())
    print(S.isAnyUpper())
