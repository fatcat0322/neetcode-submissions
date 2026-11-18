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
        r+=len(nums)
        while l<=r:
            mid=((r-l)//2+l)
            if nums[mid%len(nums)]>target:
                r=(mid-1)
            elif nums[mid%len(nums)]<target:
                l=(mid+1)
            else:
                return mid%len(nums)
        return -1
            