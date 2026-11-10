class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        heap=[]
        for num, fq in freq.items():
            heapq.heappush(heap,(fq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans=[]
        while len(heap) > 0:
            ans.append(heapq.heappop(heap)[1])
        return ans
            