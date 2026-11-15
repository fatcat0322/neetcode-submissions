class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tok=set()
        l=0
        length=0
        for r,t in enumerate(s):
            if t not in tok:
                tok.add(t)
            else:
                while t in tok:
                    tok.remove(s[l])
                    l+=1
                tok.add(t)
            cur=r-l+1
            length=max(length,cur)
        return length
        