class Solution:
    def isPalindrome(self, s: str) -> bool:
        fw=0
        bk=len(s)-1
        if len(s) == 0 or len(s)==1:
            return True
        while fw <= bk:
            if not s[fw].isalnum():
                while not s[fw].isalnum():
                    fw+=1
                    if fw>bk:
                        break
            if not s[bk].isalnum():
                while not s[bk].isalnum():
                    bk-=1
                    if fw>bk:
                        break
            if fw>bk:
                break
            if s[fw].lower() != s[bk].lower():
                return False
            fw+=1
            bk-=1
        return True