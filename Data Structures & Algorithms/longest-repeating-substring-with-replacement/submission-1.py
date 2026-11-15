class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        maxf=0
        length=0
        l=0
        for r,c in enumerate(s):
            freq[c]+=1
            maxf=max(freq[c],maxf)
            if (r-l-maxf+1>k):
                freq[s[l]]-=1
                l+=1
            length=max(length,r-l+1)
        return length