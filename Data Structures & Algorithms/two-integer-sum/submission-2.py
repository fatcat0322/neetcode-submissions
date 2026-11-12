class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif_dict={}
        for i,n in enumerate(nums):
            dif=target-n
            if dif in dif_dict:
                return [dif_dict[dif],i]
            dif_dict[n]=i
        return None