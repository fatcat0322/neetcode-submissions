class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        length=0
        l=0
        for r,c in enumerate(s):
            freq[c]+=1
            while (r-l-max(freq.values())+1>k):
                freq[s[l]]-=1
                l+=1
            length=max(length,r-l+1)
        return length