class Solution:
    def isPalindrome(self, s: str) -> bool:
        fw=''
        bk=''
        lower=[]
        for c in s:
            lower.append(c.lower() if c.isalnum() else '')
        lower="".join(lower)
        for i in range(len(lower)//2):
            if lower[i]!= lower[len(lower)-i-1]:
                return False
        return True