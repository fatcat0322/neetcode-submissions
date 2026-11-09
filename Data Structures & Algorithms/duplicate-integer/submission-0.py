class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=False
        nl=[]
        for n in nums:
            if n not in nl:
                nl.append(n)
            else:
                dup=True
                return dup
        return dup            