s = "abedabc"
p = "abc"

def calculateHash(str1):
    Prime = 3
    hashval = 0
    for i, v in enumerate(str1):
        hashval += (ord(v) - 96)*(Prime**i)
    return  hashval

def matchingString(s, p):
    Prime = 3
    j = 0
    patternLength = len(p)
    strLength = len(s)
    patternHash = calculateHash(p)
    hashValue = calculateHash(s[:patternLength-1])
    ans = []
    for i in range(patternLength-1, strLength):
        hashValue += (ord(s[i]) - 96)*(Prime**(patternLength-1))
        print(hashValue, patternHash, s[i])
        if hashValue == patternHash and p == s[j:i+1]:
            print("Pattern at",j)
            # ans.append(s[j:i+1])
        hashValue -=  ord(s[j]) - 96
        hashValue /= 3
        j+=1
    return ans

print (matchingString(s, p))