class Solution:
    def isPalindrome(self, s: str) -> bool:
        fw=''
        bk=''
        lower=[]
        for c in s:
            if (ord(c)-ord('A') >=0) and (ord(c)-ord('A') <=25):
                lower.append(c.lower())
            elif (ord(c)-ord('a') >=0) and (ord(c)-ord('a') <=25):
                lower.append(c)
            elif (ord(c)-ord('0') >=0) and (ord(c)-ord('0') <=9):
                lower.append(c)
        lower="".join(lower)
        for i in range(len(lower)//2):
            fw+=lower[i]
            bk+=lower[len(lower)-i-1]
            if fw != bk:
                return False
        return True