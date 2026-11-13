class Solution:
    def isPalindrome(self, s: str) -> bool:
        fw=0
        bk=len(s)-1
        while fw < bk:
            while fw<bk and not s[fw].isalnum():
                fw+=1
            while fw<bk and not s[bk].isalnum():
                bk-=1
            if s[fw].lower() != s[bk].lower():
                return False
            fw+=1
            bk-=1
        return True