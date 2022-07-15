def decToHex(n):
    HexDeciNumb = ""

    i = 0
    while (n!= 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            HexDeciNumb += chr(temp + 48)
        else:
            HexDeciNumb += chr(temp + 55)
        i = i + 1
        n = int(n / 16)


    reversestring = HexDeciNumb[::-1]
    print ("0x" +reversestring)


n=2545
n=10
n=128
n=1024
decToHex(n)
