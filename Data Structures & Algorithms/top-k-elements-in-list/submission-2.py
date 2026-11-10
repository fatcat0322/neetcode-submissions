class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        freq_list=[[] for i in range(len(nums)+1)]
        for num, fq in freq.items():
            freq_list[fq].append(num)
        ans=[]
        for i in range(len(freq_list)-1,0,-1):
            for n in freq_list[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans
        