def print_formatted(number):
    khoangTrang = len(str(bin(number))[2:])
    for i in range(number):
        OctalNumber = str(oct(i+1))[2:]
        HexaNumber = str(hex(i+1))[2:].upper()
        BinNumber = str(bin(i+1))[2:]
        print(str(i+1).rjust(khoangTrang," "),OctalNumber.rjust(khoangTrang," "), HexaNumber.rjust(khoangTrang," "), BinNumber.rjust(khoangTrang," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)