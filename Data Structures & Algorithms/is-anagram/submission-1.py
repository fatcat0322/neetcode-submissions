class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq=[0]*26
        t_freq=[0]*26
        for sc in s:
            s_freq[ord(sc)-ord('a')]+=1
        for tc in t:
            t_freq[ord(tc)-ord('a')]+=1
        if s_freq == t_freq:
            return True
        return False
