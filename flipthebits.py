#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
def getBinary(dec: int) -> int:
            import math
            binary = ""
            while dec != 0 and dec != 1:
                rem = str(dec % 2)
                dec = math.floor(dec / 2)
                binary = rem + binary
            binary = "1" + binary
            
            return binary
def getDecimal(bin: int) -> int:
    dec = 0
    strBin = str(bin)
    strLen = len(strBin)
    for i in range(0,strLen):
        dec  =  dec + (int(strBin[strLen-i-1])*(2**i))
    return dec
binRep = getBinary(5)
flipped = ""
for i in binRep:
    if i == "1":
        flipped = flipped + "0"
    else:
        flipped = flipped + "1"
print(binRep)
print(flipped)
print(getDecimal(flipped))
