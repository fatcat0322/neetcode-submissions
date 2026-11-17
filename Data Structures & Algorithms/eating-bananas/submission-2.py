class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            mid=(r-l)//2+l
            t=0
            for p in piles:
                t+=-(-p//mid)
            if t>h:
                l=mid+1
            else:
                r=mid-1
        return l
