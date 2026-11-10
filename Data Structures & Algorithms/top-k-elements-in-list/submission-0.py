class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        freq_l=[]
        for n in nums:
            freq[n]+=1
        for key,value in freq.items():
            freq_l.append((key,value))
        freq_l=sorted(freq_l,reverse=True ,key=lambda x: x[1])
        ans=[]
        for i in range(k):
            ans.append(freq_l[i][0])
        return ans