class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]>nums[-1]:
                l=mid+1
            else:
                r=mid-1
        return nums[l]
            