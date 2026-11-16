class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_fq=defaultdict(int)
        s2_fq=defaultdict(int)
        for c in s1:
            s1_fq[c]+=1
        for i,c in enumerate(s2):
            if c in s1_fq:
                s2_fq[c]+=1
            if i>len(s1)-1 and s2[i-len(s1)] in s1_fq:
                s2_fq[s2[i-len(s1)]]-=1
            print(s2_fq)
            if s1_fq==s2_fq:
                return True
        return False