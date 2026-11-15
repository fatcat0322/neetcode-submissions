class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tok={}
        l=0
        length=0
        for r,t in enumerate(s):
            if t in tok:
                l=max(tok[t]+1,l)
            tok[t]=r
            cur=r-l+1
            length=max(length,cur)
        return length
        