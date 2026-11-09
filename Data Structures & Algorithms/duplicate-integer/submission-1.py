class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nl=set()
        for n in nums:
            if n in nl:
                return True
            nl.add(n)
        return False            