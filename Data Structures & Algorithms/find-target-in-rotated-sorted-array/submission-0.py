class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]>nums[-1]:
                l=mid+1
            else:
                r=mid-1
        if target>nums[-1]:
            l=0
        else:
            r=len(nums)-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return -1
            